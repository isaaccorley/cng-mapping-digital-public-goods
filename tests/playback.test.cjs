const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { test } = require('node:test');
const { runInNewContext } = require('node:vm');

const source = readFileSync('animations.html', 'utf8').replace(/<\/?script>/g, '');
const flush = () => new Promise(resolve => setImmediate(resolve));

function fixture(playResults = [Promise.resolve(), Promise.resolve()], search = '') {
  const documentEvents = {};
  const windowEvents = {};
  const slideEvents = {};
  const videos = playResults.map(result => ({
    // Metadata-only loading: no canplay event arrives before play is requested.
    readyState: 1,
    currentTime: 0,
    paused: true,
    controls: false,
    playCalls: 0,
    listeners: {},
    addEventListener(name, listener) { this.listeners[name] = listener; },
    removeEventListener(name) { delete this.listeners[name]; },
    pause() { this.paused = true; },
    play() { this.playCalls++; this.paused = false; return result; },
  }));
  const slide = {
    querySelectorAll: () => videos,
    contains: video => videos.includes(video),
  };
  const emptySlide = { querySelectorAll: () => [], contains: () => false };
  let currentSlide = slide;
  const document = {
    readyState: 'loading',
    visibilityState: 'visible',
    querySelectorAll: () => videos,
    addEventListener(name, listener) { documentEvents[name] = listener; },
  };
  let config;
  const Reveal = {
    isReady: () => true,
    configure(options) { config = options; },
    getCurrentSlide: () => currentSlide,
    on(name, listener) { slideEvents[name] = listener; },
  };
  const window = {
    Reveal,
    location: { search },
    addEventListener(name, listener) { windowEvents[name] = listener; },
  };
  runInNewContext(source, { window, document, Reveal, setTimeout, URLSearchParams });
  documentEvents.DOMContentLoaded();
  return {
    videos, document, documentEvents, windowEvents, config,
    leave() {
      currentSlide = emptySlide;
      slideEvents.slidechanged({ currentSlide });
    },
    enter() {
      currentSlide = slide;
      slideEvents.slidechanged({ currentSlide });
    },
  };
}

test('conference mode keeps automatic 15-second advances enabled after interaction', () => {
  const { config } = fixture();
  assert.equal(config.autoSlide, 15000);
  assert.equal(config.autoSlideStoppable, false);
});

test('manual review disables even explicit per-slide timers', () => {
  const { config } = fixture(undefined, '?autoSlide=0');
  // Reveal treats false as a full opt-out; numeric zero still permits slide overrides.
  assert.equal(config.autoSlide, false);
});

test('CNG timing holds the cover and advances subsequent slides every 15 seconds', () => {
  const deck = readFileSync('index.qmd', 'utf8');
  const headings = deck.match(/^## .+$/gm);
  assert.equal(headings.length, 20);
  assert.ok(headings[0].includes('data-autoslide="0"'));
  assert.ok(headings.slice(1).every(heading => heading.includes('data-autoslide="15000"')));
  assert.match(deck, /auto-slide: 15000/);
  assert.match(deck, /auto-slide-stoppable: false/);
});

test('metadata-only videos start without waiting for canplay from either clip', async () => {
  const { videos } = fixture();
  await flush();
  assert.deepEqual(videos.map(video => video.playCalls), [1, 1]);
  assert.ok(videos.every(video => video.muted && !video.paused));
});

test('one pending clip does not prevent its neighbour from playing', async () => {
  const { videos } = fixture([new Promise(() => {}), Promise.resolve()]);
  await flush();
  assert.equal(videos[1].playCalls, 1);
  assert.equal(videos[1].paused, false);
});

test('blocked autoplay exposes controls without blocking the other clip', async () => {
  let rejectPlay;
  const blocked = new Promise((_, reject) => { rejectPlay = reject; });
  const { videos } = fixture([blocked, Promise.resolve()]);
  rejectPlay(new Error('Autoplay blocked'));
  await flush();
  assert.equal(videos[0].controls, true);
  assert.equal(videos[1].playCalls, 1);
});

test('leaving pauses both clips, including a late play completion', async () => {
  let finishPlay;
  const pending = new Promise(resolve => { finishPlay = resolve; });
  const f = fixture([pending, Promise.resolve()]);
  f.leave();
  f.videos[0].paused = false; // A delayed browser play request finishes after navigation.
  finishPlay();
  await flush();
  assert.ok(f.videos.every(video => video.paused));
});

test('re-entry restarts clips and returning to a visible tab resumes paused media', async () => {
  const f = fixture();
  await flush();
  f.videos.forEach(video => { video.currentTime = 5; });
  f.leave();
  f.enter();
  assert.ok(f.videos.every(video => video.currentTime === 0));
  f.videos.forEach(video => video.pause());
  f.document.visibilityState = 'hidden';
  f.documentEvents.visibilitychange();
  assert.ok(f.videos.every(video => video.paused));
  f.document.visibilityState = 'visible';
  f.documentEvents.visibilitychange();
  await flush();
  assert.ok(f.videos.every(video => !video.paused));
});

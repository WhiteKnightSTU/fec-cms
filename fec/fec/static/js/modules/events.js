
const EventEmitter2 = require('eventemitter2');
// const emitter = EventEmitter2();
// window.events = window.events || new EventEmitter2();

export default function initEvents() {
    window.events = window.events = new EventEmitter2();
    return window.events || new EventEmitter2();
}

/**
 * 
 */
import { default as FilterPanel } from '../modules/filters/filter-panel.js';
import { default as TagList } from '../modules/filters/filter-tags.js';
import { default as Calendar } from '../modules/calendar.js';
import { calendarDownload, getUrl } from '../modules/calendar-helpers.js';

// Initialize filters
var filterPanel = new FilterPanel();

// Initialize filter tags
const $tagList = new TagList({
  resultType: 'events',
  emptyText: 'all events'
}).$body;

$('.js-filter-tags').prepend($tagList);

// Initialize calendar
new Calendar({
  selector: '#calendar',
  download: '#calendar-download',
  subscribe: '#calendar-subscribe',
  url: getUrl(['calendar-dates']),
  exportUrl: calendarDownload(['calendar-dates', 'export']),
  subscribeUrl: getUrl(['calendar-dates', 'export'], '', [
    'sub'
  ]),
  filterPanel: filterPanel
});

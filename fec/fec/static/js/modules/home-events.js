
var calendarHelpers = require('./calendar-helpers');
var moment = require('moment');

var today = new Date();
var day = today.getDate();
var month = today.getMonth() + 1;
var year = today.getFullYear();
var todaysDate = year + '-' + month + '-' + day;

var eventsTemplate = require('../templates/homepage/events-and-deadlines.hbs');

// These values come from constants.py
// and need to match API parameter `calendar_category_id`

var updates = {
  '.js-next-commission-meeting': ['32', '40'],
  '.js-next-filing-deadline': ['21', '25', '26', '27'],
  '.js-next-training-or-conference': ['33', '34'],
  '.js-next-public-comment-deadline': ['23']
};

// Home Page: Events and deadlines
function HomepageEvents() {
  $.each(updates, function(eventClass, eventCategories) {
    var url = calendarHelpers.getUrl('calendar-dates', {
      sort: 'start_date',
      min_start_date: todaysDate,
      calendar_category_id: eventCategories
    });

    $.getJSON(url).done(function(events) {
      var event = events.results[0];
      var startDate = '';

      if (events.results.length > 1) {
        event = events.results[0];
        var min_date = event.start_date;

        // Filters events by location 'FEC'
        // and checks if the minimum date is equal to the returned start date
        var filtered = events.results.filter(function(event) {
          return event.location == 'FEC' && event.start_date == min_date;
        });

        // Display the location 'FEC' events first,
        // Otherwise, there's no FEC events and get the first one in the list
        if (filtered.length > 0) {
          event = filtered[0];
        }
      }

      if (typeof event !== 'undefined') {
        startDate = moment(event.start_date).format('MMMM D');
      } else {
        event = '';
      }

      $(eventClass).html(
        eventsTemplate({
          startDate: startDate,
          url: event.url,
          summary: event.summary
        })
      );
    });
  });
}

module.exports = {
  HomepageEvents: HomepageEvents
};


var tables = require('../modules/tables');
var columns = require('../modules/columns');

var electioneeringTemplate = require('../templates/communication-costs.hbs');

$(document).ready(function() {
  var $table = $('#results');
  new tables.DataTable($table, {
    autoWidth: false,
    title: 'Communication costs',
    path: ['communication_costs'],
    columns: columns.communicationCosts,
    rowCallback: tables.modalRenderRow,
    useExport: true,
    order: [[4, 'desc']],
    useFilters: true,
    callbacks: {
      afterRender: tables.modalRenderFactory(electioneeringTemplate)
    }
  });
});

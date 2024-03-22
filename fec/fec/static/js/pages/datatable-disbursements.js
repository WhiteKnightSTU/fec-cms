
import { disbursements as cols_disbursements } from '../modules/columns.js';
import { lineNumberFilters } from '../modules/filters-event.js';
import TableSwitcher from '../modules/table-switcher.js';
import { DataTable, OffsetPaginator, SeekPaginator, modalRenderFactory, modalRenderRow } from '../modules/tables.js';
import disbursementTemplate from '../templates/disbursements.hbs';

$(document).ready(function() {
  const $table = $('#results');
  new DataTable($table, {
    autoWidth: false,
    title: 'Disbursements',
    path: ['schedules', 'schedule_b'],
    columns: cols_disbursements,
    query: { sort_nulls_last: false },
    paginator: SeekPaginator,
    order: [[4, 'desc']],
    useFilters: true,
    useExport: true,
    rowCallback: modalRenderRow,
    callbacks: {
      afterRender: modalRenderFactory(disbursementTemplate)
    }
  });

  new TableSwitcher('.js-table-switcher', {
    efiling: {
      path: ['schedules', 'schedule_b', 'efile'],
      dataType: 'efiling',
      hideColumns: '.hide-efiling',
      paginator: OffsetPaginator
    },
    processed: {
      path: ['schedules', 'schedule_b'],
      dataType: 'processed',
      hideColumns: '.hide-processed',
      paginator: SeekPaginator
    }
  }).init();

  lineNumberFilters();
});

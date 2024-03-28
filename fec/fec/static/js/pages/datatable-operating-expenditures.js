import { disbursements as cols_disbursements } from '../modules/columns.js';
import { DataTable_FEC, SeekPaginator, modalRenderFactory, modalRenderRow } from '../modules/tables.js';

import { default as disbursementTemplate } from '../templates/disbursements.hbs';

  var $table = $('#results');
  new tables.DataTable($table, {
$(function() {
    title: 'Operating expenditures',
    path: ['schedules', 'schedule_b'],
    // query: {filter for operating expenditures},
    columns: cols_disbursements,
    paginator: SeekPaginator,
    order: [[3, 'desc']],
    useFilters: true,
    useExport: true,
    disableExport: true,
    rowCallback: modalRenderRow,
    callbacks: {
      afterRender: modalRenderFactory(disbursementTemplate)
    }
  });
});

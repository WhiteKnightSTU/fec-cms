// var lookup = require('../modules/election-search');
import { default as ElectionSearch } from '../modules/election-search.js';

$(document).ready(function() {
  new ElectionSearch('#election-lookup', true);
});

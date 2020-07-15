// Testing

import { buildUrl } from './helpers';
import Vue from 'vue/dist/vue.js';
import typeahead from './typeahead';
// import { now } from 'jquery';

Vue.component('election-cycle-selector', {
  props: {
    electionCycle: {
      type: Number,
      required: true
    },
    cycles: {
      type: Array,
      required: true
    }
  },
  template: `
  <fieldset class="select">
    <label for="election-year" class="breakdown__title label t-inline-block">Time period: </label>
    <select
      :value="electionCycle"
      @input="$emit('input', $event.target.value)"
      id="election-year" name="cycle" class="form-element--inline" aria-controls="top-table">
      <option
        v-for="item in cycles"
          :value="item.value"
          :selected="electionCycle == item.value ? 'selected' : false"
        >{{ item.label }}
      </option>
    </select>
</fieldset>
  `
});

Vue.component('typeahead', {
  props: {
    id: {
      type: Number,
      required: true
    },
    isDisabled: {
      type: Boolean,
      required: true
    }
  },
  template: `
    <div class="ta">
      <label class="label" v-bind:for="'pac-comparator-typeahead-' + id">Committee name or ID</label>
      <div class="combo combo--search--mini filter__typeahead">
        <ul class="dropdown__selected"></ul>
        <input
          :id="'pac-comparator-typeahead-' + id"
          :disabled="isDisabled ? 'disabled' : false"
          :aria-readonly="isDisabled"
          type="text" class="combo__input">
        <button
          :disabled="isDisabled ? 'disabled' : false"
          :aria-readonly="isDisabled"
          class="combo__button button--search button--standard" type="button">
          <span class="u-visually-hidden">Search</span>
        </button>
      </div>
    </div>`,
  computed: {
    //
  },
  mounted: function() {
    this.$nextTick(function() {
      // Initialize this typeahead
      this.el_typeahead = new typeahead.Typeahead(
        '#pac-comparator-typeahead-' + this.id,
        'committees'
      );
      // Remove the typeahead default action and assign ours
      this.el_typeahead.$input.off('typeahead:select');
      this.el_typeahead.$input.on(
        'typeahead:select',
        this.handleSelect.bind(this)
      );
    });
  },
  methods: {
    handleSelect: function(jQueryEvent, typeaheadResults) {
      this.$emit('typeahead-select', typeaheadResults, this);
    }
  }
});

Vue.component('pac-details', {
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  data: function() {
    return {
      //
    };
  },
  template: `<div
    class="committee-details">
    <h1 v-if="data.dataSummary.name">{{ data.dataSummary.name }} <span v-if="data.calc.pacType">({{ data.calc.pacType }})</span></h1>
    <h2 v-if="data.calc.totDisburseStr != ''">{{ data.calc.totDisburseStr }}</h2>
    <h3 v-if="data.calc.coverageDatesStatement != ''">{{ data.calc.coverageDatesStatement }}</h3>
    <div v-if="data.errorMessage != ''">{{ data.errorMessage }}</div>
    <div v-else-if="data.isLoading == true">
      <div colspan="2" class="overlay__container">
        <div class="overlay is-loading">&nbsp;</div>
      </div>
    </div>
  </div>`,
  methods: {
    formatAsCurrency: function(passedValue) {
      // if it's not a number, return it
      if (passedValue === '' || passedValue === null || isNaN(passedValue))
        return passedValue;
      else return '$' + passedValue.toLocaleString(); // otherwise format it as money
    }
  } // /methods
});

Vue.component('sliders', {
  props: {
    pacs: {
      type: Array,
      required: true
    }
  },
  template: `
  <table>
    <thead>
      <tr>
        <th scope="col">Expenditure type</th>
        <th scope="col">Percentage of total expenditures</th>
        <th scope="col" colspan="2">Totals</th>
      </tr>
      <tr>
        <td></td>
        <td></td>
        <th scope="col">(orange)</th>
        <th scope="col">(teal)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Operating expenditures</th>
        <td></td>
        <td class="t-right-aligned t-mono">{{ pacs[0].calc.operExpendPctStr }}<br>{{ pacs[0].calc.operExpendStr }}</td>
        <td class="t-right-aligned t-mono">{{ pacs[1].calc.operExpendPctStr }}<br>{{ pacs[1].calc.operExpendStr }}</td>
      </tr>
      <tr>
        <th scope="row">Contributions to federal candidates / committees</th>
        <td></td>
        <td class="t-right-aligned t-mono">{{ pacs[0].calc.contribsPctStr }}<br>{{ pacs[0].calc.contribsStr }}</td>
        <td class="t-right-aligned t-mono">{{ pacs[1].calc.contribsPctStr }}<br>{{ pacs[1].calc.contribsStr }}</td>
      </tr>
      <tr>
        <th scope="row">Independent expenditures</th>
        <td></td>
        <td class="t-right-aligned t-mono">{{ pacs[0].calc.indExpendPctStr }}<br>{{ pacs[0].calc.indExpendStr }}</td>
        <td class="t-right-aligned t-mono">{{ pacs[1].calc.indExpendPctStr }}<br>{{ pacs[1].calc.indExpendStr }}</td>
      </tr>
      <tr>
        <th scope="row">All other spending</th>
        <td></td>
        <td class="t-right-aligned t-mono">{{ pacs[0].calc.otherSpendingPctStr }}<br>{{ pacs[0].calc.otherSpendingStr }}</td>
        <td class="t-right-aligned t-mono">{{ pacs[1].calc.otherSpendingPctStr }}<br>{{ pacs[1].calc.otherSpendingStr }}</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td></td>
        <th scope="col" class="markers">
          <span class="marker">0%</span>
          <span class="marker">25%</span>
          <span class="marker">50%</span>
          <span class="marker">75%</span>
          <span class="marker">100%</span>
        </th>
        <td></td>
        <td></td>
      </tr>
    </tfoot>
  </table>
  `
});

new Vue({
  el: '#pac-comparator',
  data: {
    election_cycle: 2020, // Used for queries
    electionCycles: [], // Values for the <select>
    typeaheads: [{ key: 'taSlot0' }, { key: 'taSlot1' }],
    pacs: [
      {
        key: 'pacSlot0',
        calc: {}, // Calculated values
        cmteDetails: {}, // Details about the committee org
        dataDetails: {}, // Committee's financial query results
        dataSummary: { id: '', name: '' }, // Typeahead results
        errorMessage: '', // Triggers error messages
        isLoading: false // Controls visual indicator and deactivates typeahead
      },
      {
        key: 'pacSlot1',
        calc: {},
        cmteDetails: {},
        dataDetails: {},
        dataSummary: { id: '', name: '' },
        errorMessage: '',
        isLoading: false
      }
    ]
  },
  template: `<div id="pac-comparator">
    <h3>Compare nonconnected political action committee spending</h3>
    <div class="controls-holder">
      <div class="top-left">
        <election-cycle-selector
          :cycles="electionCycles"
          :election-cycle="election_cycle"
          @input="handleElectionYearChange"
        ></election-cycle-selector>
      </div>
      <div class="top-right">
        <div class="typeaheads-holder">
          <typeahead
            v-for="(item, index) in typeaheads"
            :id="index"
            :is-disabled="pacs[index].isLoading"
            :key="item.key"
            @typeahead-select=handleTypeaheadSelect
          ></typeahead>
        </div>
        <div class="committees-holder">
          <pac-details
            v-for="(item, index) in pacs"
            :data="item"
            :key="item.key"
          ></pac-details>
        </div>
      </div>
    </div>
    <div class="charts-holder">
      <sliders
        :pacs="pacs">
      </sliders>
    </div>
  </div>`,
  beforeMount: function() {
    // Build the list of election cycles
    for (let i = 2020; i >= 1980; i -= 2) {
      this.electionCycles.push({ value: i, label: `${i - 1}-${i}` });
    }
  },
  methods: {
    handleElectionYearChange: function(newValue) {
      this.election_cycle = parseInt(newValue);
      // Check the pacs that are currently loaded and load either that need it
      for (let i = 0; i < this.pacs.length; i++) {
        if (this.pacs[i].dataSummary.id != '') this.startLoadingCommitteeData(i);
      }
    },
    handleTypeaheadSelect: function(typeaheadResults, vueComponent) {
      this.pacs[vueComponent.id].dataSummary = typeaheadResults;
      this.pacs[vueComponent.id].cmteDetails = {}; // reset committee details
      this.pacs[vueComponent.id].dataDetails = {}; // reset committee data
      this.pacs[vueComponent.id].calc = {}; // reset calculated fields
      this.startLoadingCommitteeData(vueComponent.id);
    },
    handleCommitteeHeaderClick: function(
      buttonActionID,
      clickedCommitteeSlotID
    ) {
      for (let i = 0; i < this.committeeSlots.length; i++) {
        if (this.committeeSlots[i].slotID == clickedCommitteeSlotID) {
          if (buttonActionID == 'clear') {
            this.resetCommitteeSlot(this.committeeSlots[i]);
          } else {
            if (buttonActionID == 'left') {
              this.committeeSlots[i - 1].displayOrder++;
              this.committeeSlots[i].displayOrder--;
            } else if (buttonActionID == 'right') {
              this.committeeSlots[i].displayOrder++;
              this.committeeSlots[i + 1].displayOrder--;
            }
            this.committeeSlots.sort(function(a, b) {
              return a.displayOrder - b.displayOrder;
            });
            break;
          }
        }
      }
    },
    startLoadingCommitteeData: function(typeaheadsArrayPos) {
      // this.typeaheads[typeaheadsArrayPos].isDisabled = true;
      console.log('startLoadingCommitteeData(): ', typeaheadsArrayPos);

      let instance = this;
      // instance.isLoading = true;
      this.pacs[typeaheadsArrayPos].errorMessage = '';
      this.pacs[typeaheadsArrayPos].isLoading = true;
      window
        .fetch(
          buildUrl(
            [
              'committee',
              this.pacs[typeaheadsArrayPos].dataSummary.id,
              'totals'
            ],
            {
              cycle: this.election_cycle,
              per_page: 100,
              sort_null_only: false,
              sort_hide_null: false,
              sort_nulls_last: false,
              page: 1
            },
            {
              cache: 'no-cache',
              mode: 'no-cors', // TODO: change this to 'cors'
              signal: null
            }
          )
        )
        .then(response => {
          console.log('data fetch.then response: ', response);
          if (response.status !== 200)
            throw new Error('ERROR:REJECTED_DATA_REQUEST', response); // (throw error, be done)
          // else if (response.type == 'cors') throw new Error('CORS error');
          // If the response has a message, (otherwise, it's a data response)
          if (response.message)
            instance.handleCommitteeRequestRejected(
              response,
              this.pacs[typeaheadsArrayPos].dataSummary.id,
              this.election_cycle
            );
          else {
            response.json().then(data => {
              instance.handleCommitteeDataLoaded(data);
            });
          }
        }) // / then
        .catch(error => {
          instance.handleCommitteeRequestRejected(
            error,
            this.pacs[typeaheadsArrayPos].dataSummary.id,
            this.election_cycle
          );
        });
    },
    handleCommitteeDataLoaded: function(data) {
      console.log('handleCommitteeDataLoaded(): ', data);

      // Figger out where to put these details — let's loop through the pacs list until we find a matching ID
      if (data.results && data.results[0].committee_id) {
        let idToFind = data.results[0].committee_id;
        for (let i = 0; i < this.pacs.length; i++) {
          if (this.pacs[i].dataSummary.id == idToFind) {
            // Save the data details
            this.pacs[i].dataDetails = data.results[0];
            // And handle the quick-access values
            this.calcPacValues(i);
            // Check to make sure it's a non-connected PAC
            let isNoncomm = this.isNonconnectedPac(i);
            if (isNoncomm === true) {
              // We don't need to load the committee details so let's skip it
              this.pacs[i].isLoading = false;
            } else if (this.isNonconnectedPac(i) === 'maybe') {
              this.startLoadingCommitteeDetails(i);
            } else {
              this.pacs[i].errorMessage =
                'You entered a committee that is not a nonconnected PAC. Please enter an active nonconnected PAC name or ID.';
            }

            // this.pacs[i].isLoading = false;
            break; // no reason to check another
          }
        }
      }
    },
    handleCommitteeRequestRejected: function(
      error,
      requestedPacID,
      requestedElectionCycle
    ) {
      console.log('handleCommitteeRequestRejected(): ', error, requestedPacID, requestedElectionCycle);
      // Since we had a requested rejected, let's check to make sure it's still a legit request
      // (e.g., if we requested on pac-cycle combo but the user has changed the year since then, this rejection is outdated)
      if (
        requestedElectionCycle &&
        requestedElectionCycle == this.election_cycle
      ) {
        for (let i = 0; i < this.pacs.length; i++) {
          if (this.pacs[i].dataSummary.id == requestedPacID) {
            if (error.message == 'ERROR:REJECTED_DATA_REQUEST') {
              this.pacs[i].errorMessage =
                'You entered a committee that was not active during 2017-2018 period. Please enter a nonconnected PAC name or ID active during 2017-2018.';
            } else {
              this.pacs[i].errorMessage = 'HANDLE THIS';
            }
            this.pacs[i].isLoading = false;
            // re-enable the typeahead
            break; // no reason to check another
          }
        }
      } else {
        // if the election year has changed, meh, ignore this rejection
      }
    },
    startLoadingCommitteeDetails: function(typeaheadsArrayPos) {
      // this.typeaheads[typeaheadsArrayPos].isDisabled = true;
      console.log('startLoadingCommitteeDetails(): ', typeaheadsArrayPos);

      let instance = this;

      window
        .fetch(
          buildUrl(
            ['committee', this.pacs[typeaheadsArrayPos].dataSummary.id],
            {
              per_page: 100,
              sort_null_only: false,
              sort_hide_null: false,
              sort_nulls_last: false,
              page: 1
            },
            {
              cache: 'no-cache',
              mode: 'no-cors', // TODO: change this to 'cors'
              signal: null
            }
          )
        )
        .then(response => {
          console.log('details fetch.then response: ', response);
          if (response.status !== 200)
            throw new Error('ERROR:REJECTED_DETAILS_REQUEST', response); // (throw error, be done)
          // else if (response.type == 'cors') throw new Error('CORS error');
          // If the response has a message, (otherwise, it's a data response)
          // if (response.message)
          // instance.handleCommitteeRequestRejected(
          //   response,
          //   this.pacs[typeaheadsArrayPos].dataSummary.id
          // );
          if (!response.message) {
            response.json().then(data => {
              instance.handleCommitteeDetailsLoaded(data);
            });
          }
        }) // / then
        .catch(error => {
          instance.handleCommitteeRequestRejected(
            error,
            this.pacs[typeaheadsArrayPos].dataSummary.id,
            this.election_cycle
          );
        });
    },
    handleCommitteeDetailsLoaded: function(data) {
      console.log('handleCommitteeDetailsLoaded(): ', data);
      let idToFind = data.results[0].committee_id;

      for (let i = 0; i < this.pacs.length; i++) {
        // TODO pull this into its own thing so it's not a dupe
        if (this.pacs[i].dataSummary.id == idToFind) {
          // Save the data details
          this.pacs[i].cmteDetails = data.results[0];

          // Check to make sure it's a non-connected PAC
          if (this.isNonconnectedPac(i) == false)
            this.pacs[i].errorMessage =
              'You entered a committee that is not a nonconnected PAC. Please enter an active nonconnected PAC name or ID.';

          this.pacs[i].isLoading = false;
          break; // no reason to check another
        }
      }
    },
    isNonconnectedPac: function(pacSlotPos) {
      /* Valid rules to find nonconnected committees:

        1. committee type in            [O, U, V, W]
        2. committee designation NOT in [A, J, P]

        OR

        1. committee type in            [N, Q]
        2. committee designation NOT in [A, J, P]
        3. org type NOT in              [C, L, M, T, W]

      */
      let cType = this.pacs[pacSlotPos].dataDetails.committee_type;
      let cDesig = this.pacs[pacSlotPos].dataDetails.committee_designation;
      let oType = false;
      if (
        this.pacs[pacSlotPos].cmteDetails &&
        this.pacs[pacSlotPos].cmteDetails.organization_type !== undefined
      )
        oType = String(this.pacs[pacSlotPos].cmteDetails.organization_type);

      console.log('cmteDetails: ', this.pacs[pacSlotPos].cmteDetails);
      console.log('organization_type: ', this.pacs[pacSlotPos].cmteDetails.organization_type);
      console.log('cType, cDesig, oType: ', cType, cDesig, oType);

      let validCmteTypesWithOrgType = ['O', 'U', 'V', 'W'];
      let validCmteTypesWithoutOrgType = ['N', 'Q'];
      let invalidOrgTypes = ['C', 'L', 'M', 'T', 'W'];
      let invalidDesigs = ['A', 'J', 'P'];

      let toReturn = false;

      if (invalidDesigs.includes(cDesig)) {
        // If we have an invalid designation, its not nonconnected
        // We'll let toReturn stay false
      } else if (validCmteTypesWithoutOrgType.includes(cType)) {
        // If the committee type doesn't need an org type, we're safe to return
        // Designation is valid (from the if)
        toReturn = true;
      } else if (oType === false) {
        // oType is false if we don't have committee details yet (which includes org type)
        toReturn = 'maybe';
      } else if (
        validCmteTypesWithOrgType.includes(cType) &&
        !invalidOrgTypes.includes(oType)
      ) {
        // We've made it to the committee types that need an org type so we need those details
        // If oType is false, we haven't loaded the committee details yet
        toReturn = true;
      }

      console.log('isNonConnectedPac: ', toReturn);

      return toReturn;
    },
    calcPacValues: function(pacSlotPos) {
      let toReturn = {};
      let d = this.pacs[pacSlotPos].dataDetails;

      // Total disbursements
      toReturn.totDisburse = d.disbursements;
      toReturn.totDisburseStr = this.formatAsCurrency(d.disbursements);

      // PAC type
      toReturn.pacType = d.committee_type;

      // Coverage dates string
      toReturn.coverageDatesStatement = '';
      if (d.coverage_start_date && d.coverage_end_date) {
        let dateFormatOptions = {
          day: '2-digit',
          month: '2-digit',
          year: '2-digit',
          timeZone: 'America/New_York'
        };
        let startDate = new Date(d.coverage_start_date).toLocaleDateString(
          'us-EN',
          dateFormatOptions
        );
        let endDate = new Date(d.coverage_end_date).toLocaleDateString(
          'us-EN',
          dateFormatOptions
        );
        toReturn.coverageDatesStatement = `total expenditures from ${startDate}-${endDate}`;
      }

      // Operating expenditures
      toReturn.operExpend = 0;
      toReturn.operExpendStr = '';
      toReturn.operExpendPct = 0;
      toReturn.operExpendPctStr = '';
      if (d.operating_expenditures || d.operating_expenditures === 0) {
        toReturn.operExpend = d.operating_expenditures;
        toReturn.operExpendStr = this.formatAsCurrency(
          d.operating_expenditures,
          true
        );
        toReturn.operExpendPct =
          d.operating_expenditures / toReturn.totDisburse;
        toReturn.operExpendPctStr = this.percentString(toReturn.operExpendPct);
      }

      // Contributions to federal candidates / committees
      toReturn.contribs = 0;
      toReturn.contribsStr = '';
      toReturn.contribsPct = 0;
      toReturn.contribsPctStr = '';
      if (
        (d.contributions && d.contribution_refunds) ||
        (d.contributions === 0 && d.contribution_refunds === 0)
      ) {
        toReturn.contribs = d.contributions - d.contribution_refunds;
        toReturn.contribsStr = this.formatAsCurrency(toReturn.contribs, true);
        toReturn.contribsPct = toReturn.contribs / toReturn.totDisburse;
        toReturn.contribsPctStr = this.percentString(toReturn.contribsPct);
      }

      // Independent expenditures
      toReturn.indExpend = 0;
      toReturn.indExpendStr = '';
      toReturn.indExpendPct = 0;
      toReturn.indExpendPctStr = '';
      if (d.independent_expenditures || d.independent_expenditures === 0) {
        toReturn.indExpend = d.independent_expenditures;
        toReturn.indExpendStr = this.formatAsCurrency(toReturn.indExpend, true);
        toReturn.indExpendPct = toReturn.indExpend / toReturn.totDisburse;
        toReturn.indExpendPctStr = this.percentString(toReturn.indExpendPct);
      }

      // Other spending
      toReturn.otherSpending = 0;
      toReturn.otherSpendingStr = '';
      toReturn.otherSpendingPct = 0;
      toReturn.otherSpendingPctStr = '';
      // To make the code shorter, here's a list of var names included with otherSpending
      let otherSpend = [
        'coordinated_expenditures_by_party_committee',
        'fed_election_activity',
        'other_disbursements',
        'total_transfers',
        'loan_repayments_made',
        'loan_repayments_received',
        'loans_and_loan_repayments_made',
        'loans_and_loan_repayments_received',
        'loans_made',
        'refunded_individual_contributions',
        'refunded_other_political_committee_contributions',
        'refunded_political_party_committee_contributions',
        'refunds_relating_convention_exp'
      ];
      otherSpend.forEach(value => {
        console.log('otherSpend.forEach(): ', value, d[value]);
        if (d[value]) toReturn.otherSpending += d[value];
      });
      console.log('toReturn.otherSpending: ', toReturn.otherSpending);
      toReturn.otherSpendingStr = this.formatAsCurrency(toReturn.otherSpending);
      toReturn.otherSpendingPct = toReturn.otherSpending / toReturn.totDisburse;
      toReturn.otherSpendingPctStr = this.percentString(
        toReturn.otherSpendingPct
      );

      // Put the values onto this.pacs
      this.pacs[pacSlotPos].calc = toReturn;
    },
    formatAsCurrency: function(passedValue, roundToWhole) {
      // If it's invalid, just send it back
      if (passedValue === '' || passedValue === null || isNaN(passedValue))
        return passedValue;

      // Round if we should
      let toReturn = roundToWhole ? Math.round(passedValue) : passedValue;
      return '$' + toReturn.toLocaleString(); // otherwise format it as money
    },
    percentString: function(val) {
      let v = val * 100;
      return v < 1 ? '<1%' : `${Math.round(v)}%`;
    }
  }
});

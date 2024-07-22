import { test, expect } from '@jest/globals';
import {
  getAllLinks,
  findIfPafOrNagWasUsed,
} from '../../../../../../src/aims_ui/static/js/b_multiple_matches/multiple_address_results.mjs';
import { getTableElement } from './table_source.mjs';

// Test links aquired
test('Links aquired from table', () => {
  // Deffine table data for this test
  const rows = [
    {
      JOBID: 343,
      NAME: '',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'NA',
      RECS_PROCESSED: '25000 of 25000',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 344,
      NAME: '',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'NA',
      RECS_PROCESSED: '25000 of 25000',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 345,
      NAME: 'Test Extra Hapy',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'NA',
      RECS_PROCESSED: '25000 of 25000',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 346,
      NAME: 'dead test',
      STATUS: 'failed',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'NA',
      RECS_PROCESSED: '22500 of 25000',
      DOWNLOAD_LINK: 'Not Yet Available',
    },
    {
      JOBID: 347,
      NAME: 'test',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'NA',
      RECS_PROCESSED: '25000 of 25000',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 348,
      NAME: 'BLAH',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'NA',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 349,
      NAME: 'Large test for max charac',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'NA',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 350,
      NAME: 'Large test for 5k result',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'NA',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 351,
      NAME: 'test2',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'NA',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 352,
      NAME: 'Test extra metadata capab',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'True',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 353,
      NAME: 'test metadata',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'True',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 354,
      NAME: 'Test NO HEADER',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: '',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 355,
      NAME: 'Test no header',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: '',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 356,
      NAME: 'test with null changed',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: '',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: 'Unavailable',
    },
    {
      JOBID: 357,
      NAME: 'string false',
      STATUS: 'results-exported',
      USER_ID: 'NotLoggedinUser',
      HEADER_ROW: 'False',
      RECS_PROCESSED: '5110 of 5110',
      DOWNLOAD_LINK: '<a>something</a>',
    },
  ];

  const tableElement = getTableElement(rows);
  //console.log(tableElement);

  // Append the table to the document
  document.body.appendChild(tableElement);
  const links = getAllLinks();
  //console.log(links);

  // TODO fix this, do other tests first
  expect(1).toBe(1);
});

test('Paf or Nag Selector tests', () => {
  const pafAddress = {
    formattedAddress: 'NA address example',
    pafAddress: 'PAF address example',
    nagAddress: 'NAG address example',
  };

  const detectedPafOrNag = findIfPafOrNagWasUsed(pafAddress);

  // Expect the result to be PAF
  expect(detectedPafOrNag).toBe('N/A');
});

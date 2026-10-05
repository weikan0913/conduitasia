/**
 * Conduit Asia — skip GA4 + GoatCounter for site maintenance (localStorage ca_staff=1).
 * Enable:  ?ca_staff=1  on any page, or staff-analytics.html?on=1
 * Disable: ?ca_staff=0  or staff-analytics.html?off=1
 */
(function (global) {
  'use strict';

  var KEY = 'ca_staff';

  function applyQueryToggle() {
    try {
      var params = new URLSearchParams(global.location.search);
      if (params.get('ca_staff') === '1') {
        global.localStorage.setItem(KEY, '1');
      } else if (params.get('ca_staff') === '0') {
        global.localStorage.removeItem(KEY);
      }
    } catch (e) {
      /* ignore */
    }
  }

  function isStaffMode() {
    applyQueryToggle();
    try {
      return global.localStorage.getItem(KEY) === '1';
    } catch (e) {
      return false;
    }
  }

  global.__caSkipAnalytics = isStaffMode();

  global.caLoadGa4 = function (measurementId) {
    if (global.__caSkipAnalytics || !measurementId) return;
    var s = global.document.createElement('script');
    s.async = true;
    s.src =
      'https://www.googletagmanager.com/gtag/js?id=' +
      encodeURIComponent(measurementId);
    global.document.head.appendChild(s);
    global.dataLayer = global.dataLayer || [];
    function gtag() {
      global.dataLayer.push(arguments);
    }
    global.gtag = gtag;
    gtag('js', new Date());
    gtag('config', measurementId);
  };

  global.caLoadGoatCounter = function (endpoint) {
    if (global.__caSkipAnalytics || !endpoint) return;
    if (global.document.querySelector('script[data-goatcounter]')) return;
    var s = global.document.createElement('script');
    s.async = true;
    s.setAttribute('data-goatcounter', endpoint);
    s.src = 'https://gc.zgo.at/count.js';
    (global.document.body || global.document.documentElement).appendChild(s);
  };

  global.caGcEvent = function (name) {
    if (global.__caSkipAnalytics || !name) return;
    try {
      if (global.goatcounter && global.goatcounter.count) {
        global.goatcounter.count({
          path: name,
          title: 'event: ' + name,
          event: true,
        });
      }
    } catch (e) {
      /* ignore */
    }
  };
})(window);

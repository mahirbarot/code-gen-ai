/*
Template: AItech - Artificial Neural Network AI HTML Template
Author: Peacefulqode.com
Version: 1.0
Design and Developed by: Peaceful Qode
*/

// ================Landing Page=========================//

var tpj = jQuery;
if (window.RS_MODULES === undefined) window.RS_MODULES = {};
if (RS_MODULES.modules === undefined) RS_MODULES.modules = {};
RS_MODULES.modules["revslider41"] = {
   once: RS_MODULES.modules["revslider41"] !== undefined ? RS_MODULES.modules["revslider41"].once : undefined, init: function () {
      window.revapi4 = window.revapi4 === undefined || window.revapi4 === null || window.revapi4.length === 0 ? document.getElementById("rev_slider_4_1") : window.revapi4;
      if (window.revapi4 === null || window.revapi4 === undefined || window.revapi4.length == 0) { window.revapi4initTry = window.revapi4initTry === undefined ? 0 : window.revapi4initTry + 1; if (window.revapi4initTry < 20) requestAnimationFrame(function () { RS_MODULES.modules["revslider41"].init() }); return; }
      window.revapi4 = jQuery(window.revapi4);
      if (window.revapi4.revolution == undefined) { revslider_showDoubleJqueryError("rev_slider_4_1"); return; }
      revapi4.revolutionInit({
         revapi: "revapi4",
         DPR: "dpr",
         sliderLayout: "fullwidth",
         visibilityLevels: "1240,1024,778,480",
         gridwidth: "1300,1024,778,480",
         gridheight: "1080,768,550,500",
         lazyType: "smart",
         perspective: 600,
         perspectiveType: "global",
         editorheight: "1080,768,550,500",
         responsiveLevels: "1240,1024,778,480",
         progressBar: { disableProgressBar: true },
         navigation: {
            onHoverStop: false
         },
         parallax: {
            levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 46, 47, 48, 49, 50, 51, 30],
            type: "mouse",
            origo: "slidercenter",
            speed: 0
         },
         viewPort: {
            global: true,
            globalDist: "-200px",
            enable: false
         },
         fallbacks: {
            allowHTML5AutoPlayOnAndroid: true
         },
      });

   }
} // End of RevInitScript
if (window.RS_MODULES.checkMinimal !== undefined) { window.RS_MODULES.checkMinimal(); };
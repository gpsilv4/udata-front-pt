System.register(["./index-legacy.5.2.32.js","./en-legacy.5.2.3.js"],(function(e,t){"use strict";var r;return{setters:[e=>{r=e.d},null],execute:function(){function t(e){return e>1&&e<5&&1!=~~(e/10)}function n(e,r,n,s){var a=e+" ";switch(n){case"s":return r||s?"pár sekúnd":"pár sekundami";case"m":return r?"minúta":s?"minútu":"minútou";case"mm":return r||s?a+(t(e)?"minúty":"minút"):a+"minútami";case"h":return r?"hodina":s?"hodinu":"hodinou";case"hh":return r||s?a+(t(e)?"hodiny":"hodín"):a+"hodinami";case"d":return r||s?"deň":"dňom";case"dd":return r||s?a+(t(e)?"dni":"dní"):a+"dňami";case"M":return r||s?"mesiac":"mesiacom";case"MM":return r||s?a+(t(e)?"mesiace":"mesiacov"):a+"mesiacmi";case"y":return r||s?"rok":"rokom";case"yy":return r||s?a+(t(e)?"roky":"rokov"):a+"rokmi"}}var s=e("default",{name:"sk",weekdays:"nedeľa_pondelok_utorok_streda_štvrtok_piatok_sobota".split("_"),weekdaysShort:"ne_po_ut_st_št_pi_so".split("_"),weekdaysMin:"ne_po_ut_st_št_pi_so".split("_"),months:"január_február_marec_apríl_máj_jún_júl_august_september_október_november_december".split("_"),monthsShort:"jan_feb_mar_apr_máj_jún_júl_aug_sep_okt_nov_dec".split("_"),weekStart:1,yearStart:4,ordinal:function(e){return e+"."},formats:{LT:"H:mm",LTS:"H:mm:ss",L:"DD.MM.YYYY",LL:"D. MMMM YYYY",LLL:"D. MMMM YYYY H:mm",LLLL:"dddd D. MMMM YYYY H:mm",l:"D. M. YYYY"},relativeTime:{future:"za %s",past:"pred %s",s:n,m:n,mm:n,h:n,hh:n,d:n,dd:n,M:n,MM:n,y:n,yy:n}});r.locale(s,null,!0)}}}));

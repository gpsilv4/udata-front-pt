System.register(["./index-legacy.5.2.32.js","./en-legacy.5.2.3.js"],(function(_,t){"use strict";var e;return{setters:[_=>{e=_.d},null],execute:function(){var t="января_февраля_марта_апреля_мая_июня_июля_августа_сентября_октября_ноября_декабря".split("_"),n="январь_февраль_март_апрель_май_июнь_июль_август_сентябрь_октябрь_ноябрь_декабрь".split("_"),r="янв._февр._мар._апр._мая_июня_июля_авг._сент._окт._нояб._дек.".split("_"),s="янв._февр._март_апр._май_июнь_июль_авг._сент._окт._нояб._дек.".split("_"),m=/D[oD]?(\[[^[\]]*\]|\s)+MMMM?/;function i(_,t,e){var n,r;return"m"===e?t?"минута":"минуту":_+" "+(n=+_,r={mm:t?"минута_минуты_минут":"минуту_минуты_минут",hh:"час_часа_часов",dd:"день_дня_дней",MM:"месяц_месяца_месяцев",yy:"год_года_лет"}[e].split("_"),n%10==1&&n%100!=11?r[0]:n%10>=2&&n%10<=4&&(n%100<10||n%100>=20)?r[1]:r[2])}var M=function(_,e){return m.test(e)?t[_.month()]:n[_.month()]};M.s=n,M.f=t;var a=function(_,t){return m.test(t)?r[_.month()]:s[_.month()]};a.s=s,a.f=r;var u=_("default",{name:"ru",weekdays:"воскресенье_понедельник_вторник_среда_четверг_пятница_суббота".split("_"),weekdaysShort:"вск_пнд_втр_срд_чтв_птн_сбт".split("_"),weekdaysMin:"вс_пн_вт_ср_чт_пт_сб".split("_"),months:M,monthsShort:a,weekStart:1,yearStart:4,formats:{LT:"H:mm",LTS:"H:mm:ss",L:"DD.MM.YYYY",LL:"D MMMM YYYY г.",LLL:"D MMMM YYYY г., H:mm",LLLL:"dddd, D MMMM YYYY г., H:mm"},relativeTime:{future:"через %s",past:"%s назад",s:"несколько секунд",m:i,mm:i,h:"час",hh:i,d:"день",dd:i,M:"месяц",MM:i,y:"год",yy:i},ordinal:function(_){return _},meridiem:function(_){return _<4?"ночи":_<12?"утра":_<17?"дня":"вечера"}});e.locale(u,null,!0)}}}));

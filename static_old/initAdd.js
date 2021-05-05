window.onload=initAdd

// import tab classes
import {VanillaJSAdder} from './vanillaJSAdd.js';
import {VueAdder} from './vueAdd.js';
import {SimRules} from './dadSimRules.js';
//import {ReactAdder} from './reactAdd.js';


// jQuery objects for nav and tab elements
const vanillaJSTab = $("#vanillaJSTab");
const vanillaJSNav = $("#vanillaJSNav");
const vueTab = $("#vueTab");
const vueNav = $("#vueNav");
const reactTab = $("#reactTab");
const reactNav = $("#reactNav");
const rulesTab = $("#rulesTab");
const rulesNav = $("#rulesNav");

// initializ all classes and nav bar
function initAdd(){
    VanillaJSAdder.init();
    //VueAdder.init(); Not needed
    initNavBar();
}

// add click functions to nav tabs
function initNavBar(){
    vanillaJSNav.click( function() {setTab("js")});
    vueNav.click( function() {setTab("vue")});
    reactNav.click( function() {setTab("react")});
    rulesNav.click( function() {setTab("rules")});
}

// hide tabs and show clicked tab
function setTab(tab){
    vanillaJSNav.removeClass("ActiveTab");
    vueNav.removeClass("ActiveTab");
    reactNav.removeClass("ActiveTab");
    rulesNav.removeClass("ActiveTab");
    vanillaJSTab.hide();
    vueTab.hide();
    reactTab.hide();
    rulesTab.hide();
    if(tab == "js"){
        vanillaJSNav.addClass("ActiveTab");
        vanillaJSTab.show();
    } else if(tab == "vue"){
        vueNav.addClass("ActiveTab");
        vueTab.show();
    } else if(tab == "react"){
        reactNav.addClass("ActiveTab");
        reactTab.show();
    } else if(tab == "rules"){
        rulesNav.addClass("ActiveTab");
        rulesTab.show();
    }
}
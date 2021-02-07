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
}

// hide tabs and show clicked tab
function setTab(tab){
    vanillaJSNav.removeClass("ActiveTab");
    vueTab.removeClass("ActiveTab");
    reactTab.removeClass("ActiveTab");
    vanillaJSTab.hide();
    vueTab.hide();
    reactTab.hide();
    if(tab == "js"){
        vanillaJSNav.addClass("ActiveTab");
        vanillaJSTab.show();
    } else if(tab == "vue"){
        vueNav.addClass("ActiveTab");
        vueTab.show();
    } else if(tab == "react"){
        reactNav.addClass("ActiveTab");
        reactTab.show();
    }
}
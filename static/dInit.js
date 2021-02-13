window.onload=init

// import Views
import {DefView} from './dDefView.js';

// jQuery objects for nav and tab elements
const defTab = $("#defTab");
const defNav = $("#defNav");
const rulesTab = $("#rulesTab");
const rulesNav = $("#rulesNav");
const simTab = $("#simTab");
const simNav = $("#simNav");
const resultsTab = $("#resultsTab");
const resultsNav = $("#resultsNav");

// initializ all classes and nav bar
function init(){
    //DefView.init();
    initNavBar();
}

// add click functions to nav tabs
function initNavBar(){
    defNav.click( function() {setTab("def")});
    rulesNav.click( function() {setTab("rules")});
    simNav.click( function() {setTab("sim")});
    resultsNav.click( function() {setTab("results")});
}

// hide tabs and show clicked tab
function setTab(tab){
    defNav.removeClass("ActiveTab");
    rulesNav.removeClass("ActiveTab");
    simNav.removeClass("ActiveTab");
    resultsNav.removeClass("ActiveTab");
    defTab.hide();
    rulesTab.hide();
    simTab.hide();
    resultsTab.hide();
    if(tab == "def"){
        defNav.addClass("ActiveTab");
        defTab.show();
    } else if(tab == "rules"){
        rulesNav.addClass("ActiveTab");
        rulesTab.show();
    }else if(tab == "sim"){
        simNav.addClass("ActiveTab");
        simTab.show();
    } else if(tab == "results"){
        resultsNav.addClass("ActiveTab");
        resultsTab.show();
    } 
}
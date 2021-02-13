window.onload = initvillage

import { APICalls } from './api.js';
import { resource } from './resourceVue.js';
import { VBuilder} from './vueVillageBuilder.js';

function testAPI(){

    const response = APICalls.getWorkSpeed(2);
    response.then(function(results){
        console.log(results);
    });
    
}

function initvillage(){
    // let btn = document.getElementById("btn");
    // btn.addEventListener('click', function() { testAPI();});
    // const response = APICalls.getWorkSpeed();
    // response.then(function(results){
    //     console.log(results);
    // });
}
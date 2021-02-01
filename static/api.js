function apiCallWithResponse(urlStr){
    return fetch(urlStr)
    .then(function(response){
        return response.json();
    })
}

export class APICalls {
    static getWorkSpeed(villager){
        return apiCallWithResponse('/villager/workSpeed?vil=villager');
    }
}
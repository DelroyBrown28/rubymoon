$(document).ready(function () {

    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('.modal').modal();

});


window.onload = function () {

    const homepageFadein = new TimelineLite({
        paused: false
    });

    homepageFadein.fromTo('.intro_fadein', 1, {
        autoAlpha: '0'
    }, {
        delay: 0.5,
        // stagger: 0.1,
        autoAlpha: '1',
    })

    const textRollup = new TimelineLite({
        paused: false
    })

    textRollup.fromTo('.scroll_animate', 1, {
        y: '100px'
    }, {
        delay: 0.5,
        y: '0'
    })


}
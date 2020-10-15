$(document).ready(function () {

    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('.modal').modal();
    $('select').formSelect();

});


window.onload = function () {

    const homepageFadein = new TimelineLite({
        paused: false
    });

    homepageFadein.fromTo('.intro_fadein', 0.5, {
        autoAlpha: '0'
    }, {
        delay: 0.3,
        // stagger: 0.1,
        autoAlpha: '1',
    })

    const textRollup = new TimelineLite({
        paused: false
    })

    textRollup.fromTo('.scroll_animate', 1, {
        y: '100px',
        autoAlpha: '0'
    }, {
        delay: 0.5,
        y: '0',
        autoAlpha: '1'
    })


}
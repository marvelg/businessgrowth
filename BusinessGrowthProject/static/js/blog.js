$(document).ready(() => {
    $('.page-link').on('click',(event) => {
        $('.page-link').removeClass('active')
        $(event.currentTarget).addClass('active')
    })
})
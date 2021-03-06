$(document).ready(function () {
    $('a.smooth-scroll').on('click', function (event) {
        var $anchor = $(this);
        var myoffset = window.matchMedia('(max-width: 720px)').matches ? 50 : 60;

        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - myoffset
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
    $('.slider-wrap').owlCarousel({
        items: 1,
        nav: false,
        dots: false,
        rewind: true,
        autoplay: true,
        autoplayTimeout: 10000,
        autoplayHoverPause: false,
        animateIn: 'fadeIn',
        animateOut: 'fadeOut',
    });
    var dots = window.matchMedia('(max-width: 1020px)').matches;
    $('.gallery-wrap').owlCarousel({
        margin: 100,
        loop: true,
        autoWidth: true,
        items: 2,
        dots: dots,
        nav: false,
        center: true,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true,
        lazyLoad: true,
        animateIn: 'bounceInRight',
        animateOut: 'bounceInLeft',
    });
    if (window.matchMedia('(max-width: 720px)').matches) {
        var d = $('.detail');
        d.addClass('owl-carousel');
        d.owlCarousel({
            items: 1,
            nav: false,
            dots: true,
            rewind: true,
            autoplay: true,
            autoplayTimeout: 7500,
            autoplayHoverPause: false,
            animateIn: 'bounceInRight',
            animateOut: 'bounceOutLeft',
        });
        $('#responcemenu').affix({
            offset: {
                top: function () {
                    return (this.top = $('#responcemenu').position().top-$('#responcemenu').outerHeight());
                },
                bottom: function () {
                    return (this.bottom = $('footer').outerHeight(true));
                }
            }
        });
         $('#responcemenu').on('affix-top.bs.affix', function (e) {
             $('#responcemenu .navbar-collapse').collapse('hide');
         });
        $('body').scrollspy({target: '#responcemenu', offset: 50})
    } else {
        $('#affix-menu').affix({
            offset: {
                top: function () {
                    return (this.top = $('.topbar').outerHeight(true));
                },
                bottom: function () {
                    return (this.bottom = $('footer').outerHeight(true));
                }
            }
        });
        $('body').scrollspy({target: '#affix-menu', offset: 60})
    }
    $('[data-toggle="tooltip"]').tooltip();

    $('#menu').find('ul.menus a[data-first=True]').tab('show');
    $('#menu').find('.categories[data-first=True]').first().find('a').first().tab('show');
    $('#menu').find('ul.menus').on('shown.bs.tab', function (e) {
        var anch = e.target.getAttribute('href');
        $(anch).find('ul.nav a').first().first().tab('show');
    });

    $('#menu').find(".dropdown a[data-toggle='tab']").on('shown.bs.tab', function (e) {
        var anch = e.target.getAttribute('href');
        $(anch).find('ul.nav a').first().first().tab('show');
        $('#menu .dropdown a.dropdown-toggle').text($(this).text());
//        console.log(e.relatedTarget);
    });

    $('#menu').find(".dropdown a[data-toggle='tab']").click(function (e) {
        e.preventDefault();
        $('#menu .dropdown li.active').removeClass('active');
        $(this).tab('show');
    })

    $('#menu').find(".dropdown").on('hide.bs.dropdown', function (e) {
   //     console.log(e.relatedTarget);
   //     console.log(e.target);
    });

    $('.dropdown-menu a[data-first=True]').tab('show');
//    $('.dropdown a.dropdown-toggle').text($('.dropdown-menu a[data-first=True]').text());

    var offset = 500, offset_opacity = 1200, scroll_top_duration = 700, $back_to_top = $('.top');
    $(window).on('scroll', function () {
        ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('is-visible') : $back_to_top.removeClass('is-visible fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('fade-out');
        }
    });
    $back_to_top.on('click', function (event) {
        event.preventDefault();
        $('body,html').animate({
                scrollTop: 0
            }, scroll_top_duration
        );
    });
});

/*********************************************************************************

  Template Name: JuniorHome Day Care  Bootstrap 4 Template  
  Template URI: https://themeforest.net/user/hastech
  Description: JuniorHome is a beautifula and unique Day Care Bootstrap 4 template.
  Author: HasTech
  Author URI: https://hastech.company/
  Version: 1.0

  Note: This is style css.


**********************************************************************************/


/*===============================================================================
      [ INDEX ]
=================================================================================

  Scroll Up Activation
  Mobile Menu
  Wow Active
  Youtub Popup
  Testimonial Activation 01
  Testimonial Activation 02 
  Testimonial Activation 03
  Testimonial Activation 04
  Arrinval Product Activation 
  Sticky Header
  Counter Up
  Popular Activation
  Event Activation
  Event Activation 02 
  Gallery Mesonry Activation
  Blog Thumb Activation
  Home Slider Activation
  Register Form
  Login Form
  Checkout Login/Register Toggle
  Checkout Shipping Form Toggle
  Payment Method Toggle
  Home Slider With Carosel
  Countdown
  Blog Share Activation



=================================================================================
      [ END INDEX ]
================================================================================*/

(function ($) {
  'use strict';


  /*============ Scroll Up Activation ============*/
  $.scrollUp({
    scrollText: '<i class="fa fa-angle-up"></i>',
    easingType: 'linear',
    scrollSpeed: 900,
    animation: 'slide'
  });



  /*=========== Mobile Menu ===========*/

  $('nav.mainmenu__nav').meanmenu({
    meanMenuClose: 'X',
    meanMenuCloseSize: '18px',
    meanScreenWidth: '991',
    meanExpandableChildren: true,
    meanMenuContainer: '.mobile-menu',
    onePage: true
  });



  /*=========== Wow Active ===========*/

  new WOW().init();


  /*============= Youtub Popup ==============*/

  $('a.play__btn').yu2fvl();


  /*============= Cartbox Toggler ==============*/

  function cartboxToggler() {
    var trigger = $('.minicart-trigger'),
      container = $('.cartbox-wrap');
    $('<div class="body-overlay"></div>').prependTo(container);

    trigger.on('click', function (e) {
      e.preventDefault();
      container.toggleClass('is-visible');
    });
    $('.cartbox-close').on('click', function () {
      container.removeClass('is-visible');
    });
    container.find('.body-overlay').on('click', function () {
      container.removeClass('is-visible');
    });
  }
  cartboxToggler();




  /*=============  Testimonial Activation 01  ==============*/

  $(".tes__activation--1").owlCarousel({
    loop: true,
    margin: 0,
    nav: false,
    autoplay: true,
    autoplayTimeout: 3000,
    items: 1,
    dots: false,
    lazyLoad: true,
    responsive: {
      0: {
        items: 1
      },
      1920: {
        items: 1
      }
    }
  });



  /*=============  Testimonial Activation 02  ==============*/

  $(".tes__activation--2").owlCarousel({
    loop: true,
    margin: 0,
    nav: false,
    autoplay: false,
    autoplayTimeout: 3000,
    items: 1,
    dots: false,
    lazyLoad: true,
    responsive: {
      0: {
        items: 1
      },
      1920: {
        items: 1
      }
    }
  });


  /*=============  Testimonial Activation 03  ==============*/

  $(".testimonial__slide--3").owlCarousel({
    loop: true,
    nav: true,
    autoplay: false,
    autoplayTimeout: 3000,
    items: 1,
    dots: false,
    margin: 30,
    navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
    lazyLoad: true,
    responsive: {
      0: {
        items: 1
      },
      1920: {
        items: 1
      }
    }
  });


  /*=============  Testimonial Activation 04  ==============*/

  $(".testimonial__slide--4").owlCarousel({
    loop: true,
    nav: true,
    autoplay: false,
    autoplayTimeout: 3000,
    items: 1,
    dots: false,
    margin: 30,
    navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
    lazyLoad: true,
    responsive: {
      0: {
        items: 1
      },
      1920: {
        items: 1
      }
    }
  });



  /*=============  Arrinval Product Activation  ==============*/

  $(".arrival__product__activation").owlCarousel({
    loop: true,
    margin: 0,
    nav: false,
    autoplay: false,
    autoplayTimeout: 3000,
    items: 1,
    dots: true,
    lazyLoad: true,
    responsive: {
      0: {
        items: 1
      },
      1920: {
        items: 1
      }
    }
  });




  /*=========== Sticky Header ===========*/
  function stickyHeader() {
    $(window).on('scroll', function () {
      var sticky_menu = $('.sticky__header');
      var pos = sticky_menu.position();
      if (sticky_menu.length) {
        var windowpos = sticky_menu.top;
        $(window).on('scroll', function () {
          var windowpos = $(window).scrollTop();
          if (windowpos > pos.top + 250) {
            sticky_menu.addClass('is-sticky');
          } else {
            sticky_menu.removeClass('is-sticky');
          }
        });
      }
    });
  }
  stickyHeader();



  /*=========== Counter Up ===========*/

  $('.count').counterUp({
    delay: 10,
    time: 1000
  });


  /*=============  Popular Activation  ==============*/

  $(".popular__group__slide__init").owlCarousel({
    loop: true,
    nav: true,
    autoplay: false,
    autoplayTimeout: 3000,
    items: 2,
    dots: false,
    margin: 30,
    navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
    lazyLoad: true,
    responsive: {
      0: {
        items: 1
      },
      768: {
        items: 1
      },
      992: {
        items: 2
      },
      1920: {
        items: 2
      }
    }
  });


  /*=============  Event Activation  ==============*/

  $(".event__big__thumb").owlCarousel({
    loop: true,
    nav: true,
    autoplay: false,
    autoplayTimeout: 3000,
    items: 1,
    dots: false,
    margin: 30,
    navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
    lazyLoad: true,
    responsive: {
      0: {
        items: 1
      },
      1920: {
        items: 1
      }
    }
  });



  /*=============  Event Activation 02  ==============*/

  $(".activation__one").owlCarousel({
    loop: true,
    margin: 0,
    nav: true,
    autoplay: false,
    autoplayTimeout: 3000,
    items: 3,
    dots: false,
    navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
    lazyLoad: true,
    responsive: {
      0: {
        items: 1
      },

      575: {
        items: 2
      },

      768: {
        items: 2
      },
      992: {
        items: 3
      },
      1920: {
        items: 3
      }
    }
  });




  /*=============  Gallery Mesonry Activation  ==============*/

  $('.gallery__masonry__activation').imagesLoaded(function () {

    // filter items on button click
    $('.gallery__menu').on('click', 'button', function () {
      var filterValue = $(this).attr('data-filter');
      $grid.isotope({
        filter: filterValue
      });
    });

    // change is-checked class on buttons
    $('.gallery__menu button').on('click', function () {
      $('.gallery__menu button').removeClass('is-checked');
      $(this).addClass('is-checked');
      var selector = $(this).attr('data-filter');
      $containerpage.isotope({
        filter: selector
      });
      return false;
    });

    // init Isotope
    var $grid = $('.masonry__wrap').isotope({
      itemSelector: '.gallery__item',
      percentPosition: true,
      transitionDuration: '0.7s',
      masonry: {
        // use outer width of grid-sizer for columnWidth
        columnWidth: 1,
      }
    });


  });



  /*=============  Blog Thumb Activation  ==============*/
  
  $('.blog__thumb__active').slick({
    arrows: true,
    infinite: true,
    pauseOnHover: true,
    slidesToShow: 1,
    slideToScroll: 1,
    fade: true,
    speed: 600,
    prevArrow: '<button class="dcare-arrow dacre-prev"><i class="fa fa-angle-left"></i></button>',
    nextArrow: '<button class="dcare-arrow dcare-next"><i class="fa fa-angle-right"></i></button>',
  });


  /*=============  Home Slider Activation  ==============*/

  $('.slide--active').slick({
    arrows: true,
    infinite: true,
    pauseOnHover: true,
    slidesToShow: 1,
    slideToScroll: 1,
    fade: true,
    speed: 600,
    prevArrow: '<button class="dcare-arrow dacre-prev"><i class="fa fa-angle-left"></i></button>',
    nextArrow: '<button class="dcare-arrow dcare-next"><i class="fa fa-angle-right"></i></button>',
  });


  /*============= Register Form ==============*/

  function registerForm() {
    var trigger = $('.accountbox-trigger'),
      container = $('.accountbox-wrapper');
    $('<div class="body-overlay"></div>').prependTo(container);

    trigger.on('click', function (e) {
      e.preventDefault();
      container.addClass('is-visible');
    });

    $('.body-overlay').on('click', function () {
      container.removeClass('is-visible');
    });

    $('span.accountbox-close-button').on('click', function () {
      container.removeClass('is-visible');
    });

  }
  registerForm();




  /*============= Login Form ==============*/

  function logInForm() {
    var trigger = $('.login-trigger'),
      container = $('.login-wrapper');
    $('<div class="body-overlay"></div>').prependTo(container);

    trigger.on('click', function (e) {
      e.preventDefault();
      container.addClass('is-visible');
    });

    $('.body-overlay').on('click', function () {
      container.removeClass('is-visible');
    });

    $('span.accountbox-close-button').on('click', function () {
      container.removeClass('is-visible');
    });

  }
  logInForm();



  /*============= Checkout Login/Register Toggle ==============*/

  function checkoutLoginToggle() {
    var checkoutMethodList = $('.checkout-method-list li');
    checkoutMethodList.on('click', function () {
      var form = $(this).data('form');
      if (!$(this).hasClass('active')) {
        $('.checkout-method-list li').removeClass('active');
        $(this).addClass('active');
        $('.checkout-method form').slideUp(500);
        $('.' + form).delay(500).slideDown();
      }
    });
  }
  checkoutLoginToggle();



  /*============= Checkout Shipping Form Toggle ==============*/

  function checkoutShippingToggle() {
    var shipingFormToggle = $('.shipping-form-toggle');
    var shipingForm = $('.shipping-form');
    shipingFormToggle.on('click', function () {
      if ($(this).hasClass('active')) {
        $(this).removeClass('active');
        shipingForm.slideUp();
      } else {
        $(this).addClass('active');
        shipingForm.slideDown();
      }
    });
  }
  checkoutShippingToggle();


  /*============= Payment Method Toggle ==============*/

  function paymentMethodToggle() {
    var paymentMethodList = $('.payment-method-list li');
    var paymentFormToggle = $('.payment-form-toggle');
    var paymentForm = $('.payment-form');
    paymentMethodList.on('click', function () {
      paymentMethodList.removeClass('active');
      $(this).addClass('active');
      if ($(this).hasClass('payment-form-toggle')) {
        paymentForm.slideDown();
      } else {
        paymentForm.slideUp();
      }
    });
  }
  paymentMethodToggle();




  /*============= Home Slider With Carosel ==============*/

  if ($('.slide__carosel').length) {
    $('.slide__carosel').owlCarousel({
      loop: true,
      margin: 0,
      nav: true,
      autoplay: false,
      navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
      autoplayTimeout: 10000,
      items: 1,
      dots: false,
      lazyLoad: true,
      responsive: {
        0: {
          items: 1
        },
        600: {
          items: 1
        },
      }
    });
  }


  /*============= Countdown ==============*/

  $('[data-countdown]').each(function () {
    var $this = $(this),
      finalDate = $(this).data('countdown');
    $this.countdown(finalDate, function (event) {
      $this.html(event.strftime('<span class="dcare-count days"><span class="count-inner"><span class="time-count">%-D</span> <p>Days</p></span></span> <span class="dcare-count hour"><span class="count-inner"><span class="time-count">%-H</span> <p>Hours</p></span></span> <span class="dcare-count minutes"><span class="count-inner"><span class="time-count">%M</span> <p>Minutes</p></span></span> <span class="dcare-count second"><span class="count-inner"><span class="time-count">%S</span> <p>Seconds</p></span></span>'));
    });
  });




  /*============= Blog Share Activation ==============*/

  $(".blog__share").each(function () {

    $(this).on("click", function (e) {
      e.preventDefault();
      $(this).find(".dacre__social__link").toggleClass("clicked");
    });
  });








})(jQuery);
(function ($) {
    $.fn.extend({
        showHide: function () {
            $(this).animate( {opacity: 1}, 500 );
            return this;
        }
    });

    $('.noscript').hide();
    var $env_instructions = $('#env-instructions');
    var $env_options = $('#env-options');
    $env_options.show();
    $env_instructions.children().eq(0).siblings().hide();

    $env_options.on('click', 'div', function (e) {
        if (! $(this).hasClass('active')) {
            $(this).addClass('active').siblings().removeClass('active');
            var id = $(this).index() - 1;
            // $env_instructions.children('div').eq(id).showHide();
            $env_instructions.children('div').eq(id).show().siblings().hide();
        }
    })

    var $msg = $('.msg');
    var $register_buttons = $('#content a.register-button.disabled,' +
        '#content a.register-button.postponed');
    $msg.hide();

    // disable redirect on disabled anchor buttons
    $register_buttons.on('click', function (e) {
        e.preventDefault();
        $(this).nextAll('.msg').fadeIn(200);
    });


}) (jQuery);

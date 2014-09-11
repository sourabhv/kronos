(function ($) {

	var $content = $('#content')
	var $lt = $('#lt')

	$(window).on('focus', function () {
		$('body').addClass('activated');
		$(this).off('focus');
	})

	$(window).on('resize', function (e) {
		var h = ($(window).innerHeight() - $lt.outerHeight()) * 0.4;
		$content.css({'margin-top': h + 'px'})
	}).trigger('resize');

}) (jQuery);

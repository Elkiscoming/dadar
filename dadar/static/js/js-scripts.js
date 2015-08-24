var id;
var num = 0;
var preload = 4;
var maxCount = 30;
var preloader = $('#preloader');

var showImage = function (number) {
    var image = $('#image-' + number);
    if (image.length) {
        preloader.hide();
        image.fadeIn("slow");
    }
    else
        preloader.show();
};
var showNewImage = function (prevNumber, nextNumber) {
    $('#image-' + prevNumber).hide();
    showImage(nextNumber);
};
var loadImage = function (number, isHidden) {
    $.get('image/' + id + '/' + number, function (data, status, xhr) {
        var image = $('<img>');
        image.attr('src', JSON.parse(data)['image'] );
        image.css('width', '100%');

        var div = $('<div>');
        div.attr('class', 'col l12 waves-effect waves-light waves-block');
        div.attr('id', 'image-' + number);
        div.css('position', 'absolute');
        if (isHidden)
            div.hide();

        image.appendTo(div);
        div.appendTo('#images');

        if (number == num) {
            showImage(number);
        }
    });
};
if (navigator.geolocation) { // device can return its location
    navigator.geolocation.getCurrentPosition(function (position) {
        console.log(position.coords.latitude);
        console.log(position.coords.longitude);
        console.log('init/' + position.coords.latitude + ',' + position.coords.longitude);
        $.get('init/' + position.coords.latitude + ',' + position.coords.longitude, function (data, status, xhr) {
            id = parseInt(data);
            loadImage(0, false);
            for (var i = 1; i <= preload; i++)
                loadImage(i, true);
        });
    });
}
$('#left-arrow').click(function () {
    showNewImage(num, (num < maxCount - 1 ? ++num : num));
    if (num + preload < maxCount)
        loadImage(num + preload, true);
});
$('#right-arrow').click(function () {
    showNewImage(num, (num > 0 ? --num : num));
});
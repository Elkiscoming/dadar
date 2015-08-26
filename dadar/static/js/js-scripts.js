var id;
var num = 0;
var preload = 29;
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
var loadImage = function (number) {
    $.get('image/' + id + '/' + number, function (data, status, xhr) {
        var image = $('<img>');
        image.attr('src', JSON.parse(data)['image'] );
        image.css('width', '100%');

        var container = $('<div>');
        container.attr('class', '');
        container.css('position', 'relative');

        var card = $('<div>');
        card.attr('class', 'card');

        var imageCard = $('<div>');
        imageCard.attr('class', 'card-image');

        var cardContent = $('<div>');
        cardContent.attr('class', 'card-content');

        var title = $('<p>');
        title.html(JSON.parse(data)['name']);

        var button = $('<a>');
        button.attr('class', 'btn-floating btn-large');
        button.css('position', 'absolute');
        /*button.css('top', '2%');
        button.css('left', '2%');
        */
        button.css('transform', 'translate(-50%, -50%)');
        button.css('opacity', '0.5');

        button.appendTo(container);

        title.appendTo(cardContent);

        image.appendTo(imageCard);
        imageCard.appendTo(card);
        cardContent.appendTo(card);
        card.appendTo(container);
        container.appendTo('#images-' + number % 3);
    });
};
if (navigator.geolocation) { // device can return its location
    navigator.geolocation.getCurrentPosition(function (position) {
        console.log(position.coords.latitude);
        console.log(position.coords.longitude);
        console.log('init/' + position.coords.latitude + ',' + position.coords.longitude);
        $.get('init/' + position.coords.latitude + ',' + position.coords.longitude, function (data, status, xhr) {
            id = parseInt(data);
//            loadImage(0);
            for (var i = 0; i <= preload; i++)
                loadImage(i);
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
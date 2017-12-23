var $teamContent = $('.team');

$teamContent.on('show.bs.collapse', function() {

    $teamContent.find('.collapse.show').collapse('hide');
});
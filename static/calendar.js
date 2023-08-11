document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: [FullCalendarInteraction, FullCalendarDayGrid],
        initialView: 'dayGridMonth',
        events: '/events'
    });
    calendar.render();

    // Обработчик для кнопки "Events"
    var showEventsButton = document.getElementById('showEventsButton');
    var eventsModal = document.getElementById('eventsModal');
    var eventsList = document.getElementById('eventsList');

    showEventsButton.addEventListener('click', function () {
        eventsList.innerHTML = ''; // Очищаем список событий перед отображением

        // Получаем события с сервера
        fetch('/events')
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    eventsList.innerHTML = '<ul>';
                    data.forEach(event => {
                        eventsList.innerHTML += '<li>' + event.title + ' - ' + event.start + '</li>';
                    });
                    eventsList.innerHTML += '</ul>';
                } else {
                    eventsList.innerHTML = 'No events available.';
                }
                eventsModal.style.display = 'block'; // Отображаем модальное окно
            });
    });
});


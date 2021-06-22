actors_number = 5  # how many actors to display
directors_number = 2  # how many directors to display
help_text = "КиноНавигатор\n\n " \
            "Я могу быстро найти много полезной информации о любом фильме, " \
            "а также помочь с поиском самых популярных фильмов любого жанра.\n\n" \
            "Для того, чтобы начать, просто отправь мне название интересующего тебя фильма " \
            "(я понимаю не только русский, но и английский язык) или воспользуйся кнопками ниже.\n\n" \
            "Также ты можешь пользоваться следующими командами для поиска различных фильмов:\n" \
            "• Отправь команду /popular для поиска популярных фильмов, в том числе " \
            "среди различных жанров\n" \
            "• Отправь команду /top_rated для поиска самых рейтинговых фильмов, в том числе " \
            "среди различных жанров\n" \
            "• Отправь команду /upcoming для поиска фильмов, которые скоро выйдут в кино, в том числе " \
            "среди различных жанров\n" \
            "• Отправь команду /help, чтобы в любой момент прочитать эту инструкцию ещё раз"
months = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
          "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]
movies_to_display = 10  # how many movies to display
trailer_links = {
    "Youtube": 'https://www.youtube.com/watch?v={}',
    "Vimeo": 'https://vimeo.com/{}'
}
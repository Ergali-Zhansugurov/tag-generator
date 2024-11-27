from internal.core.usecases.gen_tags import GenerateTags

def main():
    print("work the facking code")
    reviews = ["Купила для собственного развития, читала много положительных отзывов. Будет полезна как для новичков, так и для опытных разработчиков. Книга пришла в хорошем состоянии, комфортный шрифт для чтения и в подарок вложили магнитную закладку, мелочь, но приятно. Спасибо, flip, за работу. Спасибо за то что у вас имеются книги, которых днём с огнём не найдешь в наших книжных магазинах.",
                "Всем доволен. Книга красивая, бумага хорошая, доставка в обещанный срок и даже быстрее. По поводу самой книги, пока прочел только первые 100 страниц - соответсвует ожиданиям. Для тех кто хочет узнать о том как писать хороший чистый код - самое то.",
                  "Плохой код может работать, но он будет мешать развитию проекта и компании-разработчика, требуя дополнительные ресурсы на поддержку и «укрощение». Каким же должен быть код? Эта книга полна реальных примеров, позволяющих взглянуть на код с различных направлений: сверху вниз, снизу вверх и даже изнутри. Вы узнаете много нового о коде. Более того, научитесь отличать хороший код от плохого, узнаете, как писать хороший код и как преобразовать плохой код в хороший. Книга состоит из трех частей. Сначала вы познакомитесь с принципами, паттернами и приемами написания чистого кода. Затем приступите к практическим сценариям с нарастающей сложностью — упражнениям по чистке кода или преобразованию проблемного кода в менее проблемный. И только после этого перейдете к самому важному — концентрированному выражению сути этой книги — набору эвристических правил и «запахов кода». Именно эта база знаний описывает путь мышления в процессе чтения, написания и чистки кода."]
    tag_generator = GenerateTags(threshold=0.8)
    result = tag_generator.execute(reviews=reviews)
    print(result)

if __name__ == "__main__":
    main()
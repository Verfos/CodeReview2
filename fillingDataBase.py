from main import *

db.create_all()

q1 = Question(2, 1)
db.session.add(q1)

q2 = Question(2, 2)
db.session.add(q2)

q3 = Question(2, 3)
db.session.add(q3)

q4 = Question(2, 4)
db.session.add(q4)

q5 = Question(2, 5)
db.session.add(q5)

q6 = Question(2, 6)
db.session.add(q6)

q7 = Question(2, 7)
db.session.add(q7)

q8 = Question(2, 8)
db.session.add(q8)

q9 = Question(2, 9)
db.session.add(q9)

q10 = Question(2, 10)
db.session.add(q10)

q11 = Question(2, 11)
db.session.add(q11)

q12 = Question(2, 12)
db.session.add(q12)

q13 = Question(2, 13)
db.session.add(q13)

q14 = Question(2, 14)
db.session.add(q14)

q15 = Question(2, 15)
db.session.add(q15)

q16 = Question(2, 16)
db.session.add(q16)

q17 = Question(2, 17)
db.session.add(q17)

q18 = Question(4, 18)
db.session.add(q18)

q19 = Question(4, 19)
db.session.add(q19)

q20 = Question(2, 20)
db.session.add(q20)


a1 = Answer(1, 1, "Я люблю планировать свой день", 1)
db.session.add(a1)

a2 = Answer(2, 2, "Я люблю действовать спонтанно", 1)
db.session.add(a2)

a3 = Answer(1, 1, "Мне лучше, когда работать надо быстро, не замедляясь и не отступая.", 2)
db.session.add(a3)

a4 = Answer(2, 2, "Мне лучше даётся медленная и вдумчивая работа.", 2)
db.session.add(a4)

a5 = Answer(1, 1, "В целом я обладаю равномерной работоспособностью.", 3)
db.session.add(a5)

a6 = Answer(2, 2, "Живу периодическими подъёмами и спадами энергии.", 3)
db.session.add(a6)

a7 = Answer(1, 1, "При необходимости я легко справлюсь с повседневным бытом.", 4)
db.session.add(a7)

a8 = Answer(2, 2, "Повседневная текучка меня так угнетает, что я часто запускаю быт.", 4)
db.session.add(a8)

a9 = Answer(1, 1, "Я всегда спрашиваю себя, почему мне нравится или не нравится этот человек.", 5)
db.session.add(a9)

a10 = Answer(2, 2, "Вопрос, как он (она) ко мне относится, я задаю себе только при необходимости.", 5)
db.session.add(a10)

a11 = Answer(1, 3, "Без труда вступаю в разговор и высказываю своё мнение.", 6)
db.session.add(a11)

a12 = Answer(2, 4, "Ожидаю удобного момента, чтобы высказаться.", 6)
db.session.add(a12)

a13 = Answer(1, 3, "Если работа не пошла, недолго думая переключусь на другую деятельность.", 7)
db.session.add(a13)

a14 = Answer(2, 4, "Несделанная работа долго не идёт у меня из головы.", 7)
db.session.add(a14)

a15 = Answer(1, 3, "Мне проще реализовывать или внедрить, чем придумать что-то с нуля.", 8)
db.session.add(a15)

a16 = Answer(2, 4, "Мне проще придумать что-то, чем воплощать его в повседневную реальность.", 8)
db.session.add(a16)

a17 = Answer(1, 3, "Главную информацию о человеке я получаю от выражения его лица или интонаций.", 9)
db.session.add(a17)

a18 = Answer(2, 4, "В оценке людей я доверяю лишь документам и независимым характеристикам.", 9)
db.session.add(a18)

a19 = Answer(1, 2, "Мне бывает легче понять других, чем свой собственный характер.", 10)
db.session.add(a19)

a20 = Answer(2, 4, "Мне более понятны собственные поступки, чем мотивы других людей.", 10)
db.session.add(a20)

a21 = Answer(1, 5, "Если надо, могу долго заниматься одним и тем же, пока не завершу его.", 11)
db.session.add(a21)

a22 = Answer(2, 6, "Не могу себя заставить заниматься одним и тем же делом долго.", 11)
db.session.add(a22)

a23 = Answer(1, 5, "Хорошо воспринимаю лишь конкретную и наглядно представимую информацию.", 12)
db.session.add(a23)

a24 = Answer(2, 6, "Хорошо воспринимаю абстрактную информацию, которая требует воображения.", 12)
db.session.add(a24)

a25 = Answer(1, 5, "Нередко моё первое впечатление о человеке впоследствии подтверждается.", 13)
db.session.add(a25)

a26 = Answer(2, 6, "Не стану судить о человеке по своим первым субъективным впечатлениям.", 13)
db.session.add(a26)

a27 = Answer(1, 5, "Принимаюсь за новые и новые дела, как только разобрался со старыми.", 14)
db.session.add(a27)

a28 = Answer(2, 6, "Всё время сдерживаю круг своих забот, чтобы со всем справиться.", 14)
db.session.add(a28)

a29 = Answer(1, 5, "В основном действую так, как предварительно настроился.", 15)
db.session.add(a29)

a30 = Answer(2, 6, "Действую часто спонтанно, как сложится ситуация.", 15)
db.session.add(a30)

a31 = Answer(1, 7, "Мои предложения отличаются конкретностью и опытом решения подобных задач.", 16)
db.session.add(a31)

a32 = Answer(2, 8, "Мои предложения отличаются необычностью и учётом отдалённых последствий.", 16)
db.session.add(a32)

a33 = Answer(1, 7, "Я сразу чувствую, если кому-то не нравлюсь, даже если он это скрывает.", 17)
db.session.add(a33)

a34 = Answer(2, 8, "Я долго сомневаюсь, прежде чем удостоверюсь, что ко мне относятся с антипатией.", 17)
db.session.add(a34)

a35 = Answer(1, 7, "Нередко сожалею, что проявил излишнюю активность.", 18)
db.session.add(a35)

a36 = Answer(2, 8, "Нередко отмечаю, что мне надо было быть более активным.", 18)
db.session.add(a36)

a37 = Answer(3, 7, "Чтобы выполнить скучную, но необходимую работу, мне приходится заставлять себя.", 18)
db.session.add(a37)

a375 = Answer(4, 8, "Чтобы выполнить скучную работу, мне надо периодически переключаться или отвлекаться.", 18)
db.session.add(a375)

a38 = Answer(1, 7, "Мне нравится помечтать или представить ситуацию с другой, неожиданной стороны.", 19)
db.session.add(a38)

a39 = Answer(2, 8, "Размышляя о ситуации, я стараюсь представить её наглядно и во всех подробностях.", 19)
db.session.add(a39)

a40 = Answer(3, 7, "От меня очень трудно скрыть обиду или недовольство.", 19)
db.session.add(a40)

a41 = Answer(4, 8, "Обиду или недовольство я замечаю, когда её проявляют открыто.", 19)
db.session.add(a41)

a42 = Answer(1, 7, "Я - человек в целом открытый.", 20)
db.session.add(a42)

a43 = Answer(2, 8, "Я - человек в целом сдержанный.", 20)
db.session.add(a43)


db.session.commit()
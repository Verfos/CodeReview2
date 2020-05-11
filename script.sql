//Скрипт для создания и заполнения БД
//создали БД

sqlite3 database.db 
.exit()

//заполняем
sqlite3 database.db
INSERT INTO question VALUES(1,2,1);
INSERT INTO question VALUES(2,2,2);
INSERT INTO question VALUES(3,2,3);
INSERT INTO question VALUES(4,2,4);
INSERT INTO question VALUES(5,2,5);
INSERT INTO question VALUES(6,2,6);
INSERT INTO question VALUES(7,2,7);
INSERT INTO question VALUES(8,2,8);
INSERT INTO question VALUES(9,2,9);
INSERT INTO question VALUES(10,2,10);
INSERT INTO question VALUES(11,2,11);
INSERT INTO question VALUES(12,2,12);
INSERT INTO question VALUES(13,2,13);
INSERT INTO question VALUES(14,2,14);
INSERT INTO question VALUES(15,2,15);
INSERT INTO question VALUES(16,2,16);
INSERT INTO question VALUES(17,2,17);
INSERT INTO question VALUES(18,4,18);
INSERT INTO question VALUES(19,4,19);
INSERT INTO question VALUES(20,2,20);

INSERT INTO Answer VALUES (1,1,1,"Я люблю планировать свой день",1);
INSERT INTO Answer VALUES (2,2,2,"Я люблю действовать спонтанно",1);
INSERT INTO Answer VALUES (3,1,1,"Мне лучше, когда работать надо быстро, не замедляясь и не отступая.",2);
INSERT INTO Answer VALUES (4,2,2,"Мне лучше даётся медленная и вдумчивая работа.",2);
INSERT INTO Answer VALUES (5,1,1,"В целом я обладаю равномерной работоспособностью.",3);
INSERT INTO Answer VALUES (6,2,2,"Живу периодическими подъёмами и спадами энергии.",3);
INSERT INTO Answer VALUES (7,1,1,"При необходимости я легко справлюсь с повседневным бытом.",4);
INSERT INTO Answer VALUES (8,2,2,"Повседневная текучка меня так угнетает, что я часто запускаю быт.",4);
INSERT INTO Answer VALUES (9,1,1,"Я всегда спрашиваю себя, почему мне нравится или не нравится этот человек.",5);
INSERT INTO Answer VALUES (10,2,2,"Вопрос, как он (она) ко мне относится, я задаю себе только при необходимости.",5);
INSERT INTO Answer VALUES (11,1,3,"Без труда вступаю в разговор и высказываю своё мнение.",6);
INSERT INTO Answer VALUES (12,2,4,"Ожидаю удобного момента, чтобы высказаться.",6);
INSERT INTO Answer VALUES (13,1,3,"Если работа не пошла, недолго думая переключусь на другую деятельность.",7);
INSERT INTO Answer VALUES (14,2,4,"Несделанная работа долго не идёт у меня из головы.",7);
INSERT INTO Answer VALUES (15,1,3,"Мне проще реализовывать или внедрить, чем придумать что-то с нуля.",8);
INSERT INTO Answer VALUES (16,2,4,"Мне проще придумать что-то, чем воплощать его в повседневную реальность.",8);
INSERT INTO Answer VALUES (17,1,3,"Главную информацию о человеке я получаю от выражения его лица или интонаций.",9);
INSERT INTO Answer VALUES (18,2,4,"В оценке людей я доверяю лишь документам и независимым характеристикам.",9);
INSERT INTO Answer VALUES (19,1,2,"Мне бывает легче понять других, чем свой собственный характер.",10);
INSERT INTO Answer VALUES (20,2,4,"Мне более понятны собственные поступки, чем мотивы других людей.",10);
INSERT INTO Answer VALUES (21,1,5,"Если надо, могу долго заниматься одним и тем же, пока не завершу его.",11);
INSERT INTO Answer VALUES (22,2,6,"Не могу себя заставить заниматься одним и тем же делом долго.",11);
INSERT INTO Answer VALUES (23,1,5,"Хорошо воспринимаю лишь конкретную и наглядно представимую информацию.",12);
INSERT INTO Answer VALUES (24,2,6,"Хорошо воспринимаю абстрактную информацию, которая требует воображения.",12);
INSERT INTO Answer VALUES (25,1,5,"Нередко моё первое впечатление о человеке впоследствии подтверждается.",13);
INSERT INTO Answer VALUES (26,2,6,"Не стану судить о человеке по своим первым субъективным впечатлениям.",13);
INSERT INTO Answer VALUES (27,1,5,"Принимаюсь за новые и новые дела, как только разобрался со старыми.",14);
INSERT INTO Answer VALUES (28,2,6,"Всё время сдерживаю круг своих забот, чтобы со всем справиться.",14);
INSERT INTO Answer VALUES (29,1,5,"В основном действую так, как предварительно настроился.",15);
INSERT INTO Answer VALUES (30,2,6,"Действую часто спонтанно, как сложится ситуация.",15);
INSERT INTO Answer VALUES (31,1,7,"Мои предложения отличаются конкретностью и опытом решения подобных задач.",16);
INSERT INTO Answer VALUES (32,2,8,"Мои предложения отличаются необычностью и учётом отдалённых последствий.",16);
INSERT INTO Answer VALUES (33,1,7,"Я сразу чувствую, если кому-то не нравлюсь, даже если он это скрывает.",17);
INSERT INTO Answer VALUES (34,2,8,"Я долго сомневаюсь, прежде чем удостоверюсь, что ко мне относятся с антипатией.",17);
INSERT INTO Answer VALUES (35,1,7,"Нередко сожалею, что проявил излишнюю активность.",18);
INSERT INTO Answer VALUES (36,2,8,"Нередко отмечаю, что мне надо было быть более активным.",18);
INSERT INTO Answer VALUES (37,3,7,"Чтобы выполнить скучную, но необходимую работу, мне приходится заставлять себя.",18);
INSERT INTO Answer VALUES (38,4,8,"Чтобы выполнить скучную работу, мне надо периодически переключаться или отвлекаться.",18);
INSERT INTO Answer VALUES (39,1,7,"Мне нравится помечтать или представить ситуацию с другой, неожиданной стороны.",19);
INSERT INTO Answer VALUES (40,2,8,"Размышляя о ситуации, я стараюсь представить её наглядно и во всех подробностях.",19);
INSERT INTO Answer VALUES (41,3,7,"От меня очень трудно скрыть обиду или недовольство.",19);
INSERT INTO Answer VALUES (42,4,8,"Обиду или недовольство я замечаю, когда её проявляют открыто.",19);
INSERT INTO Answer VALUES (43,1,7,"Я - человек в целом открытый.",20);
INSERT INTO Answer VALUES (44,2,8,"Я - человек в целом сдержанный.",20);

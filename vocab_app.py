#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中級へ行こう (第2版) - Ung dung on tu vung bai 1-10
Chay:  python vocab_app.py      (Python 3.8+, chi dung thu vien co san: tkinter)
"""
import difflib
import random
import re
import unicodedata
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk, messagebox

# ----------------------------------------------------------------------------
# DU LIEU:  chu viet (kanji/katakana) | hiragana | nghia tieng Viet
# ----------------------------------------------------------------------------
VOCAB_RAW = """
#1
ファストフード|ふぁすとふーど|đồ ăn nhanh
点|てん|điểm
メニュー|めにゅー|thực đơn
代表的な|だいひょうてきな|có tính tiêu biểu, đại diện
ハンバーガー|はんばーがー|bánh mì hăm-bơ-gơ
フライドポテト|ふらいどぽてと|khoai tây chiên
スープ|すーぷ|món súp
種類|しゅるい|chủng loại
～兆円|～ちょうえん|~ nghìn tỉ yên
理由|りゆう|lý do
手軽に|てがるに|một cách dễ dàng, thuận tiện
しかし|しかし|nhưng
このような|このような|như thế này
カロリー|かろりー|ca-lo
生活習慣病|せいかつしゅうかんびょう|bệnh do thói quen sinh hoạt
増やす|ふやす|(làm) tăng
表示する|ひょうじする|hiển thị, ghi, đề
適当な|てきとうな|thích hợp
体重|たいじゅう|trọng lượng cơ thể
多くの|おおくの|nhiều
伝統的な|でんとうてきな|có tính truyền thống
最も|もっとも|nhất
非常に|ひじょうに|rất
観光客|かんこうきゃく|khách tham quan, khách du lịch
食パン|しょくぱん|bánh mì
焼き鳥|やきとり|thịt gà nướng
回転ずし|かいてんずし|sushi băng chuyền
大好きな|だいすきな|rất thích
一度に|いちどに|một lần, một lúc
あっというまに|あっというまに|vèo một cái, chẳng mấy chốc
期間限定|きかんげんてい|giảm giá có thời hạn, khuyến mãi có thời hạn
中学２年生|ちゅうがくにねんせい|học sinh năm 2 trung học
もったいない|もったいない|phí, phí hoài
無駄遣い|むだづかい|sử dụng lãng phí
健康グッズ|けんこうぐっず|sản phẩm chăm sóc sức khỏe
数年前|すうねんまえ|vài năm về trước
サムライ|さむらい|Samurai
作品|さくひん|tác phẩm
フォー|ふぉー|phở
ヌードル|ぬーどる|mì sợi
#2
ストーブ|すとーぶ|lò sưởi
ガスコンロ|がすこんろ|bếp ga
揺れ|ゆれ|(sự) rung lắc
揺れがおさまる|ゆれがおさまる|lắng xuống, ngừng [rung lắc]
慌てる|あわてる|vội vã, hấp tấp
食料|しょくりょう|lương thực
その他|そのほか|ngoài ra
万一|まんいち|lỡ như, phòng khi (trường hợp xấu xảy ra)
連絡方法|れんらくほうほう|cách thức liên lạc
避難場所|ひなんばしょ|địa điểm sơ tán
津波注意報|つなみちゅういほう|thông báo đề phòng sóng thần
避難訓練|ひなんくんれん|tập huấn sơ tán lánh nạn
不思議な|ふしぎな|kỳ lạ
幸福感|こうふくかん|cảm giác hạnh phúc
幸福感を持つ|こうふくかんをもつ|có cảm giác hạnh phúc
どんどん|どんどん|càng ngày càng
#3
親|おや|bố mẹ
携帯電話|けいたいでんわ|điện thoại di động
スマートホン|すまーとほん|điện thoại thông minh, smartphone (viết tắt: スマホ)
調査|ちょうさ|điều tra khảo sát
小学生|しょうがくせい|học sinh tiểu học
パーセント|ぱーせんと|phần trăm (%)
中学生|ちゅうがくせい|học sinh trung học cơ sở
専用|せんよう|dành riêng
タブレット|たぶれっと|máy tính bảng
大人|おとな|người lớn
ブランド|ぶらんど|hàng hiệu
見かける|みかける|bắt gặp, nhìn thấy
これら|これら|những cái này
高価な|こうかな|đắt giá
数|かず|số
年々|ねんねん|hằng năm
王様|おうさま|vua chúa
割合|わりあい|tỉ lệ
～行目|～ぎょうめ|dòng thứ ~
困った|こまった|khó khăn, rắc rối
人たち|ひとたち|những người
謝る|あやまる|xin lỗi, nhận lỗi
サボる|さぼる|trốn học
自由|じゆう|(sự) tự do
自由な|じゆうな|tự do
食べ放題|たべほうだい|ăn thoả thích
鬼|おに|con quỷ
棒|ぼう|cây gậy
怒る|おこる|tức giận
ほっぺた|ほっぺた|má
また|また|ngoài ra
表す|あらわす|thể hiện, diễn đạt
専門|せんもん|chuyên môn
なぜなら|なぜなら|tại là vì
#4
イメージ|いめーじ|hình ảnh, ấn tượng
訪れる|おとずれる|đến thăm
旅行者|りょこうしゃ|khách du lịch
実際に|じっさいに|trên thực tế
来日する|らいにちする|đến Nhật Bản
〜のイメージを持つ|〜のいめーじをもつ|có ấn tượng
表|ひょう|bảng biểu
人々|ひとびと|mọi người
礼儀正しい|れいぎただしい|lễ nghĩa, lễ phép, lịch sự
ポイント|ぽいんと|số điểm
〜に加えて|〜にくわえて|thêm vào
第～位|だい～い|vị trí thứ ~
おもてなしの心|おもてなしのこころ|lòng hiếu khách
都市|とし|đô thị
景観|けいかん|cảnh quan
ユネスコ無形文化遺産|ゆねすこむけいぶんかいさん|Di sản văn hóa phi vật thể do UNESCO công nhận
登録する|とうろくする|đăng ký
今後|こんご|thời gian tới
交通機関|こうつうきかん|phương tiện giao thông
発達する|はったつする|phát triển
治安がいい|ちあんがいい|an ninh tốt
生活水準|せいかつすいじゅん|mức sống
ショッピング|しょっぴんぐ|mua sắm
納豆|なっとう|món Natto, món đậu tương lên men
グラフ|ぐらふ|đồ thị
朝食をとる|ちょうしょくをとる|ăn sáng
オレンジジュース|おれんじじゅーす|nước cam
一気に|いっきに|đột biến, một lần, một hơi
外食する|がいしょくする|ăn ngoài
テーマパーク|てーまぱーく|khu giải trí
満足する|まんぞくする|hài lòng, thỏa mãn
和服|わふく|trang phục truyền thống Nhật
民芸品|みんげいひん|đồ thủ công mỹ nghệ truyền thống
化粧品|けしょうひん|đồ trang điểm
香水|こうすい|nước hoa
医薬品|いやくひん|dược phẩm
複数回答|ふくすうかいとう|có thể lựa chọn nhiều câu trả lời
日本食|にほんしょく|món ăn Nhật Bản, ẩm thực Nhật Bản
観光|かんこう|tham quan, du lịch
観光地|かんこうち|khu du lịch
電子機器|でんしきき|đồ điện tử
技術|ぎじゅつ|kỹ thuật
技術が進む|ぎじゅつがすすむ|tiến bộ kỹ thuật
文字|もじ|chữ viết, văn tự
～市|～し|thành phố ～
天丼|てんどん|cơm Tendon (cơm phủ tôm Tempura)
カツ丼|かつどん|cơm Katsudon (cơm phủ thịt lợn chiên xù)
明るい|あかるい|vui vẻ, sáng sủa
所|ところ|chỗ, điểm, mặt
新鮮な|しんせんな|tươi
#5
睡眠|すいみん|giấc ngủ, (việc) ngủ
～過ぎ|～すぎ|quá ~
～時がある|～ときがある|có lúc ～, có khi ~
ストレッチする|すとれっちする|vươn vai, vươn người
羊|ひつじ|con cừu
その他|そのた|khác
夜中|よなか|nửa đêm
目が覚める|めがさめる|tỉnh giấc
遅くまで|おそくまで|đến khuya, đến muộn
活動する|かつどうする|hoạt động
通勤|つうきん|đi làm
減少する|げんしょうする|giảm
体の不調|からだのふちょう|cơ thể mệt mỏi
不調を訴える|ふちょうをうったえる|kêu ca, phàn nàn mệt
自然に|しぜんに|tự nhiên
昼間|ひるま|buổi trưa
動かす|うごかす|vận động
～に関して|～にかんして|về ~
神経質な|しんけいしつな|bận tâm, lo lắng
声がよく出る|こえがよくでる|giọng sẽ hay
危険|きけん|nguy hiểm
蒸し暑い|むしあつい|oi bức
満足度|まんぞくど|mức độ hài lòng
暮らしやすさ|くらしやすさ|dễ sống
環境|かんきょう|môi trường
梅雨|つゆ|mùa mưa
カップラーメン|かっぷらーめん|mì ăn liền (đóng gói trong cốc hoặc bát)
できあがる|できあがる|làm xong
世の中|よのなか|trên đời này, trong thế gian
バカな|ばかな|ngu ngốc
年末|ねんまつ|cuối năm
宗教|しゅうきょう|tôn giáo
関係がある|かんけいがある|có liên quan
サンダル|さんだる|dép xăng đan
神聖な|しんせいな|thần thánh, linh thiêng
食欲|しょくよく|cảm giác thèm ăn
進路|しんろ|con đường học lên tiếp
面接|めんせつ|phỏng vấn
仕方|しかた|cách, cách thức
増す|ます|tăng thêm
ストレスがたまる|すとれすがたまる|bị tích tụ stress
売り|うり|đặc điểm, lợi thế
アンケートをとる|あんけーとをとる|lấy ý kiến khảo sát
#6
胃カメラ|いかめら|máy nội soi dạ dày
乾電池|かんでんち|pin khô
サインペン|さいんぺん|bút dạ dùng để ký
せんす|せんす|quạt nan gấp
インスタントコーヒー|いんすたんとこーひー|cà phê hòa tan
当時|とうじ|khi đó
注目する|ちゅうもくする|chú ý, gây sự chú ý
特許|とっきょ|bằng sáng chế
特許を取る|とっきょをとる|lấy bằng sáng chế
別の|べつの|khác
検査|けんさ|kiểm tra, xét nghiệm
政治家|せいじか|chính trị gia
提出する|ていしゅつする|nộp
単位|たんい|điểm học phần
単位を取る|たんいをとる|lấy tín chỉ
資格|しかく|chứng chỉ, tư cách
資格を取る|しかくをとる|lấy [chứng chỉ]
開発する|かいはつする|phát triển
ダイナマイト|だいなまいと|thuốc nổ, dynamite
～氏|～し|ông/bà ~
建築家|けんちくか|kiến trúc sư
災害救助|さいがいきゅうじょ|cứu trợ thiên tai thảm họa
企業|きぎょう|doanh nghiệp
大雨|おおあめ|mưa lớn
車両|しゃりょう|toa tàu
安全|あんぜん|an toàn
後悔する|こうかいする|ân hận
すっかり|すっかり|hoàn toàn
数学嫌い|すうがくぎらい|ghét toán
重い病気|おもいびょうき|bệnh nặng
退学する|たいがくする|thôi học, bỏ học
猛勉強する|もうべんきょうする|học rất căng, học rất chăm chỉ
英語に苦労する|えいごにくろうする|vận lộn, vất vả với Tiếng Anh
体調|たいちょう|tình trạng cơ thể
スリッパ|すりっぱ|dép lê đi trong nhà
ティッシュ|てぃっしゅ|giấy ăn
タグ|たぐ|nhãn, mác
ジャケット|じゃけっと|áo jacket
畳|たたみ|chiếu Tatami
～円札|～えんさつ|tờ ~ yên
くしゃくしゃになる|くしゃくしゃになる|nhăn nhúm
からからになる|からからになる|khô khốc
芯|しん|lõi
尖った|とがった|nhọn
名前をつける|なまえをつける|đặt tên
変更する|へんこうする|thay đổi
今では|いまでは|ngày nay, bây giờ
#7
温暖化|おんだんか|hiện tượng trái đất ấm dần
砂漠化|さばくか|hiện tượng sa mạc hóa
自分たち|じぶんたち|bản thân chúng ta, chính chúng ta
守る|まもる|bảo vệ
～というN|～というN|N gọi là ~
意識|いしき|ý thức
意識が生まれる|いしきがうまれる|ý thức được hình thành
以前|いぜん|trước đây
考え|かんがえ|suy nghĩ, quan điểm
リサイクル運動|りさいくるうんどう|phong trào vận động tái chế
～のだ|～のだ|dạng thường của「～んです」(mang nghĩa giải thích)
十分|じゅうぶん|hoàn toàn, đầy đủ
市町村|しちょうそん|các quận huyện thành phố
～と呼びかける|～とよびかける|kêu gọi ~
新聞紙|しんぶんし|giấy báo
今回|こんかい|lần này
次回|じかい|lần tới, lần tiếp theo
休暇|きゅうか|nghỉ phép
前もって|まえもって|trước
～時代|～じだい|thời ~
エンジニア|えんじにあ|kỹ sư
研修|けんしゅう|tập huấn
応援ソング|おうえんそんぐ|bài hát cổ vũ
名所|めいしょ|nơi nổi tiếng
中古|ちゅうこ|đồ cũ
日帰り旅行|ひがえりりょこう|đi du lịch trong ngày
貯める|ためる|để dành
日本語能力試験|にほんごのうりょくしけん|kỳ thi năng lực tiếng Nhật
願書|がんしょ|đơn xin
デジタルカメラ|でじたるかめら|máy ảnh kỹ thuật số
映画館|えいがかん|rạp chiếu phim
お願い|おねがい|xin, nhờ vả
専門学校|せんもんがっこう|trường dạy nghề
そろえる|そろえる|chuẩn bị đầy đủ, tập hợp hết
使用済み|しようずみ|đã sử dụng
食用油|しょくようあぶら|dầu ăn
ペットボトル|ぺっとぼとる|chai nhựa
牛乳パック|ぎゅうにゅうぱっく|hộp sữa
コピー用紙|こぴーようし|giấy photocopy
トイレットペーパー|といれっとぺーぱー|giấy vệ sinh
資源ごみ|しげんごみ|rác tái chế
例えば|たとえば|ví dụ
リサイクルボックス|りさいくるぼっくす|thùng đựng rác tái chế
#8
あいづち|あいづち|phản ứng, lời nói hoặc cử chỉ thể hiện đang lắng nghe người khác nói trong hội thoại
うなずく|うなずく|gật gù
合図|あいず|dấu hiệu
だから|だから|vì vậy
賛成する|さんせいする|tán thành
不安な|ふあんな|bất an
誤解する|ごかいする|hiểu nhầm
黙る|だまる|im lặng
あいづちを打つ|あいづちをうつ|nói đệm [aizuchi] (nói những từ đệm khi ai đó đang nói thể hiện sự chú ý lắng nghe của người nghe)
さまざまな|さまざまな|đa dạng, nhiều loại, nhiều mặt, khác nhau
おしゃべり|おしゃべり|nói chuyện
音楽を流す|おんがくをながす|bật nhạc
発言する|はつげんする|phát ngôn, bày tỏ ý kiến
運転免許|うんてんめんきょ|bằng lái xe
運転免許を取る|うんてんめんきょをとる|lấy bằng lái xe
訪ねる|たずねる|đến thăm
うちの子|うちのこ|con tôi
違和感|いわかん|cảm giác (khác thường / không ổn / lạ lạ)
違和感を持つ|いわかんをもつ|có cảm giác (lạ lắm / không quen / sai sai)
外出する|がいしゅつする|đi ra ngoài
喫茶コーナー|きっさこーなー|quầy giải khát
ラーメン|らーめん|mì Ramen
家庭|かてい|gia đình
ごちそうになる|ごちそうになる|được thết đãi
アジア文学|あじあぶんがく|văn học Châu Á
博士論文|はくしろんぶん|luận văn tiến sĩ
作家|さっか|nhà văn
ベストセラー|べすとせらー|sách bán chạy nhất
連絡手段|れんらくしゅだん|phương tiện liên lạc
オーケー|おーけー|OK
身振り|みぶり|động tác cơ thể
反対に|はんたいに|ngược lại
首|くび|cổ, đầu
首を振る|くびをふる|lắc đầu
#9
男|おとこ|nam
女|おんな|nữ
女性|じょせい|nữ giới, phụ nữ
職場|しょくば|nơi làm việc
男性|だんせい|nam giới, đàn ông
看護婦|かんごふ|y tá, điều dưỡng viên (nữ)
保母|ほぼ|cô nuôi dạy trẻ, bảo mẫu
職業|しょくぎょう|nghề nghiệp
名称|めいしょう|tên gọi
看護師|かんごし|y tá, điều dưỡng viên
保育士|ほいくし|nhân viên nuôi dạy trẻ, giáo viên
建築|けんちく|xây dựng
運転手|うんてんしゅ|tài xế, người lái xe
車掌|しゃしょう|nhân viên phục vụ trong tàu xe
男女|だんじょ|nam nữ
区別|くべつ|phân biệt
目を向ける|めをむける|nhìn vào
家事|かじ|việc nhà
労働|ろうどう|lao động
〜程度|〜ていど|khoảng chừng ~
調査結果|ちょうさけっか|kết quả điều tra khảo sát
AではなくB|AではなくB|không phải A mà là B
進んで|すすんで|tích cực
分担する|ぶんたんする|đảm nhận
共働き|ともばたらき|cùng đi làm
食事作り|しょくじづくり|nấu nướng
建築現場|けんちくげんば|công trường xây dựng
呼び名|よびな|tên gọi
普及|ふきゅう|phổ biến
体力|たいりょく|thể lực
月・水・金|げつ・すい・きん|thứ hai, thứ tư, thứ sáu
生む|うむ|đẻ, sinh
曜日|ようび|thứ
少子化|しょうしか|tình trạng xã hội ít trẻ con
一人暮らし|ひとりぐらし|sống một mình
姪|めい|cháu gái
甥|おい|cháu trai
苦手な|にがてな|không thích, ghét, kém về ~, không giỏi ~
コック|こっく|đầu bếp
島国|しまぐに|quốc đảo
〜に分かれる|〜にわかれる|được chia làm ~
南北に長い|なんぼくにながい|kéo dài theo chiều Bắc–Nam
弓|ゆみ|cung tên, cánh cung
〜のような形|〜のようなかたち|hình dạng giống như ~
気候|きこう|khí hậu
温暖な|おんだんな|ấm áp
地方|ちほう|địa phương, vùng
１年中|いちねんじゅう|quanh năm
独特な|どくとくな|đặc thù
行事|ぎょうじ|lễ hội
大陸|たいりく|đại lục
半島|はんとう|bán đảo
東西|とうざい|Đông Tây
雨季|うき|mùa mưa
乾季|かんき|mùa khô
熱帯|ねったい|nhiệt đới
スコール|すこーる|mưa rào
隠す|かくす|cất giấu
上司|じょうし|sếp
遅刻する|ちこくする|đến muộn
分別する|ぶんべつする|phân loại
ボランティア活動|ぼらんてぃあかつどう|hoạt động tình nguyện
いつまでも|いつまでも|lúc nào cũng
育児休暇|いくじきゅうか|nghỉ (chăm con / nuôi con nhỏ / thai sản)
寝坊する|ねぼうする|ngủ quên
問題が生まれる|もんだいがうまれる|[vấn đề] nảy sinh
しかたがない|しかたがない|không còn cách nào khác
確かに|たしかに|đúng là
両方|りょうほう|cả hai
したがって|したがって|vì vậy
#10
敬語|けいご|kính ngữ
乱れる|みだれる|bị loạn
感じる|かんじる|cảm nhận
食事の場|しょくじのば|nơi ăn uống
本来|ほんらい|vốn dĩ, đúng ra thì
変化する|へんかする|thay đổi
気にする|きにする|bận tâm
この機会に|このきかいに|nhân cơ hội này
話題|わだい|đề tài (nói chuyện)
ロケ地|ろけち|địa điểm quay
校長先生|こうちょうせんせい|thầy/cô hiệu trưởng
副校長先生|ふくこうちょうせんせい|thầy/cô hiệu phó
丁寧に|ていねいに|cẩn thận, kỹ càng, lịch sự
クラス分け|くらすわけ|phân lớp
結果|けっか|kết quả
生き方|いきかた|cách sống
話し合い|はなしあい|nói chuyện với nhau
送別会|そうべつかい|buổi chia tay
分ける|わける|chia
教授|きょうじゅ|giáo sư
通信販売|つうしんはんばい|bán hàng qua (mạng / bưu điện / điện thoại / internet), bán hàng từ xa
食品|しょくひん|thực phẩm, đồ ăn
青色LED|あおいろえるいーでぃー|đèn LED xanh dương
短時間に|たんじかんに|trong thời gian ngắn
マイカー|まいかー|xe ô tô riêng
バスツアー|ばすつあー|du lịch bằng xe buýt
カーシェアリング|かーしぇありんぐ|dịch vụ dùng chung xe ô tô
早朝出勤する|そうちょうしゅっきんする|đi làm từ sáng sớm
突然|とつぜん|bỗng nhiên
花びら|はなびら|cánh hoa
舞い落ちる|まいおちる|rụng, rơi
飛ぶ|とぶ|bay
気象衛星|きしょうえいせい|vệ tinh khí tượng
事実|じじつ|sự thực
預かる|あずかる|giữ, trông giữ
尊敬語|そんけいご|tôn kính ngữ
謙譲語|けんじょうご|khiêm nhường ngữ
模範的な|もはんてきな|mang tính (kiểu mẫu / gương mẫu), chuẩn mực
私語|しご|nói chuyện riêng
嫌がる|いやがる|ghét
教科書|きょうかしょ|sách giáo khoa
標語|ひょうご|khẩu hiệu
～ようだった|～ようだった|có vẻ ~
"""

# ----------------------------------------------------------------------------
# MO HINH DU LIEU + HAM XU LY CHUOI
# ----------------------------------------------------------------------------
CJK = re.compile(r"[\u3400-\u9fff]")
LATIN = re.compile(r"[A-Za-z]")
PUNCT = re.compile(r"[\s\u3000~～〜・、。，,.()（）\[\]「」『』“”\"'…!！?？]")

FIELDS = ("vi", "hira", "kanji")
FIELD_LABEL = {"vi": "Nghĩa", "hira": "Hiragana", "kanji": "Kanji / chữ viết"}


class Word:
    def __init__(self, lesson, w, r, vi):
        self.lesson = lesson
        self.w = w            # chu viet (kanji / katakana / hiragana)
        self.r = r            # cach doc hiragana
        self.vi = vi          # nghia tieng Viet
        self.has_kanji = bool(CJK.search(w))
        self.testable = not LATIN.search(r)   # bo cac mau cau co chu A, B, N...

    def fields(self):
        return ("vi", "hira", "kanji") if self.has_kanji else ("vi", "hira")

    def get(self, f):
        return {"vi": self.vi, "hira": self.r, "kanji": self.w}[f]


def parse_vocab(raw):
    words, lesson = [], 0
    for line in raw.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            lesson = int(line[1:])
            continue
        w, r, vi = [p.strip() for p in line.split("|", 2)]
        words.append(Word(lesson, w, r, vi))
    return words


WORDS = parse_vocab(VOCAB_RAW)


def kata2hira(s):
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)


def norm_jp(s, hira=False):
    s = unicodedata.normalize("NFKC", s)
    s = PUNCT.sub("", s)
    return kata2hira(s) if hira else s


def strip_accents(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def norm_vi(s):
    return re.sub(r"[^a-z0-9]+", " ", strip_accents(s)).strip()


def meaning_variants(ans):
    base = ans.replace("~", " ")
    no_par = re.sub(r"\([^)]*\)|\[[^\]]*\]", "", base)
    out = set()
    for text in (base, no_par):
        out.add(norm_vi(text))
        for part in re.split(r"[,;/]", text):
            out.add(norm_vi(part))
    out.discard("")
    return out


def meaning_ok(user, ans):
    u = norm_vi(user)
    if not u:
        return False
    for v in meaning_variants(ans):
        if u == v:
            return True
        if len(u) >= 4 and difflib.SequenceMatcher(None, u, v).ratio() >= 0.88:
            return True
    return False


def build_questions(words, qset, aset, n):
    words = list(words)
    random.shuffle(words)
    out = []
    for wd in words:
        av = wd.fields()
        pairs = [(s, t) for s in qset for t in aset if s != t and s in av and t in av]
        if pairs:
            s, t = random.choice(pairs)
            out.append((wd, s, t))
    return out[:n]


# ----------------------------------------------------------------------------
# UNG DUNG
# ----------------------------------------------------------------------------
GREEN = "#1b7f3b"
RED = "#c0392b"
GREY = "#5f6b7a"
FRONT_MAP = {"Kanji": "kanji", "Hiragana": "hira", "Nghĩa": "vi", "Ngẫu nhiên": "rand"}


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("中級へ行こう – Ôn từ vựng bài 1-10")
        self.geometry("1120x740")
        self.minsize(960, 640)

        fams = set(tkfont.families())

        def pick(cands, default):
            for c in cands:
                if c in fams:
                    return c
            return default

        default_family = tkfont.nametofont("TkDefaultFont").actual("family")
        self.JP = pick(["Yu Gothic UI", "Yu Gothic", "Meiryo UI", "Meiryo", "MS Gothic",
                        "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Noto Sans CJK JP",
                        "Noto Sans JP", "IPAexGothic", "TakaoGothic", "VL Gothic"], default_family)
        self.VN = pick(["Segoe UI", "Arial", "Helvetica Neue", "DejaVu Sans"], default_family)

        # chi muc: field -> {text: [Word,...]}  (de chap nhan tu dong am / dong nghia)
        self.index = {f: {} for f in FIELDS}
        for w in WORDS:
            for f in w.fields():
                self.index[f].setdefault(w.get(f), []).append(w)

        st = ttk.Style(self)
        st.configure("Treeview", font=(self.JP, 12), rowheight=30)
        st.configure("Treeview.Heading", font=(self.VN, 11, "bold"))
        st.configure("TNotebook.Tab", font=(self.VN, 11), padding=(14, 6))
        for s in ("TLabel", "TCheckbutton", "TRadiobutton", "TButton"):
            st.configure(s, font=(self.VN, 11))
        st.configure("TLabelframe.Label", font=(self.VN, 11, "bold"))

        self.lesson_vars = {i: tk.BooleanVar(value=(i == 1)) for i in range(1, 11)}

        self.build_sidebar()
        self.nb = ttk.Notebook(self)
        self.nb.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)
        self.tab_list = ttk.Frame(self.nb, padding=10)
        self.tab_flash = ttk.Frame(self.nb, padding=10)
        self.tab_test = ttk.Frame(self.nb, padding=10)
        self.nb.add(self.tab_list, text="📖  Danh sách từ")
        self.nb.add(self.tab_flash, text="🃏  Flashcard")
        self.nb.add(self.tab_test, text="✍  Kiểm tra")

        self.build_list_tab(self.tab_list)
        self.build_flash_tab(self.tab_flash)
        self.build_test_tab(self.tab_test)

        self.bind_all("<Left>", lambda e: self.flash_key(-1))
        self.bind_all("<Right>", lambda e: self.flash_key(+1))
        self.bind_all("<space>", lambda e: self.flash_key(0))
        self.bind_all("<Return>", self.on_return)
        self.bind_all("<KP_Enter>", self.on_return)
        for i in range(1, 5):
            self.bind_all(f"<Key-{i}>", lambda e, k=i - 1: self.on_number(k))

        self.on_selection_changed()

    # ---------------------------------------------------------------- helpers
    def font(self, field, size, bold=False):
        fam = self.VN if field == "vi" else self.JP
        return (fam, size, "bold") if bold else (fam, size)

    def selected_words(self):
        sel = {i for i, v in self.lesson_vars.items() if v.get()}
        return [w for w in WORDS if w.lesson in sel]

    # ---------------------------------------------------------------- sidebar
    def build_sidebar(self):
        side = ttk.Frame(self, padding=12)
        side.pack(side="left", fill="y")
        ttk.Label(side, text="Chọn bài", font=(self.VN, 13, "bold")).pack(anchor="w", pady=(0, 8))
        for i in range(1, 11):
            n = sum(1 for w in WORDS if w.lesson == i)
            ttk.Checkbutton(side, text=f"第{i}課  ({n} từ)", variable=self.lesson_vars[i],
                            command=self.on_selection_changed).pack(anchor="w", pady=2)
        ttk.Separator(side).pack(fill="x", pady=10)
        ttk.Button(side, text="Chọn tất cả", command=lambda: self.set_all(True)).pack(fill="x", pady=2)
        ttk.Button(side, text="Bỏ chọn hết", command=lambda: self.set_all(False)).pack(fill="x", pady=2)
        self.lbl_count = ttk.Label(side, text="", foreground=GREY, wraplength=170)
        self.lbl_count.pack(anchor="w", pady=12)

    def set_all(self, val):
        for v in self.lesson_vars.values():
            v.set(val)
        self.on_selection_changed()

    def on_selection_changed(self):
        words = self.selected_words()
        self.lbl_count.config(text=f"Đã chọn: {len(words)} từ")
        self.revealed = set()
        self.refresh_list()
        self.reset_deck()
        self.update_pool_label()

    # ================================================================= LIST TAB
    def build_list_tab(self, parent):
        self.revealed = set()
        top = ttk.Frame(parent)
        top.pack(fill="x")
        ttk.Label(top, text="Tìm:").pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *a: self.refresh_list())
        ttk.Entry(top, textvariable=self.search_var, width=22).pack(side="left", padx=(4, 18))
        ttk.Label(top, text="Hiện cột:").pack(side="left")
        self.show_vars = {}
        for key, label in (("kanji", "Kanji"), ("hira", "Hiragana"), ("vi", "Nghĩa")):
            v = tk.BooleanVar(value=True)
            self.show_vars[key] = v
            ttk.Checkbutton(top, text=label, variable=v, command=self.on_show_change).pack(side="left", padx=4)

        frame = ttk.Frame(parent)
        frame.pack(fill="both", expand=True, pady=8)
        cols = ("lesson", "kanji", "hira", "vi")
        self.tree = ttk.Treeview(frame, columns=cols, show="headings", selectmode="browse")
        for c, text, wd, stretch in (("lesson", "Bài", 50, False), ("kanji", "Kanji / chữ viết", 230, False),
                                     ("hira", "Hiragana", 260, False), ("vi", "Nghĩa tiếng Việt", 400, True)):
            self.tree.heading(c, text=text)
            self.tree.column(c, width=wd, stretch=stretch, anchor="w" if c != "lesson" else "center")
        sb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        self.tree.bind("<Double-1>", self.toggle_reveal)
        ttk.Label(parent, foreground=GREY,
                  text="Mẹo: bỏ tick một cột để che đi và tự kiểm tra; nhấp đúp vào dòng để xem đáp án của dòng đó.").pack(anchor="w")

    def on_show_change(self):
        self.revealed = set()
        self.refresh_list()

    def row_values(self, idx, w):
        show = idx in self.revealed
        hid = "• • •"
        return (w.lesson,
                w.w if (show or self.show_vars["kanji"].get()) else hid,
                w.r if (show or self.show_vars["hira"].get()) else hid,
                w.vi if (show or self.show_vars["vi"].get()) else hid)

    def refresh_list(self):
        if not hasattr(self, "tree"):
            return
        self.tree.delete(*self.tree.get_children())
        q = self.search_var.get().strip()
        qn = norm_vi(q)
        for w in self.selected_words():
            if q and not (q in w.w or q in w.r or q in w.vi or (qn and qn in norm_vi(w.vi))
                          or kata2hira(q) in w.r):
                continue
            idx = WORDS.index(w)
            self.tree.insert("", "end", iid=str(idx), values=self.row_values(idx, w))

    def toggle_reveal(self, event):
        iid = self.tree.identify_row(event.y)
        if not iid:
            return
        idx = int(iid)
        if idx in self.revealed:
            self.revealed.discard(idx)
        else:
            self.revealed.add(idx)
        self.tree.item(iid, values=self.row_values(idx, WORDS[idx]))

    # ============================================================= FLASHCARD TAB
    def build_flash_tab(self, parent):
        self.deck, self.fidx, self.flipped, self.cur_front = [], 0, False, "kanji"
        top = ttk.Frame(parent)
        top.pack(fill="x")
        ttk.Label(top, text="Mặt trước hiện:").pack(side="left")
        self.fc_front = tk.StringVar(value="Kanji")
        cb = ttk.Combobox(top, textvariable=self.fc_front, values=list(FRONT_MAP), width=12, state="readonly")
        cb.pack(side="left", padx=6)
        cb.bind("<<ComboboxSelected>>", lambda e: (self.focus_set(), self.goto(self.fidx)))
        ttk.Button(top, text="🔀 Xáo trộn", command=self.shuffle_deck).pack(side="left", padx=10)
        ttk.Button(top, text="↺ Theo thứ tự sách", command=self.reset_deck).pack(side="left")
        self.fc_counter = ttk.Label(top, text="", foreground=GREY)
        self.fc_counter.pack(side="right")

        white = "#ffffff"
        self.card = tk.Frame(parent, bg=white, highlightthickness=2, highlightbackground="#9aa5b1", cursor="hand2")
        self.card.pack(fill="both", expand=True, pady=12)
        inner = tk.Frame(self.card, bg=white)
        inner.place(relx=0.5, rely=0.5, anchor="center")
        self.fc_main = ttk.Label(inner, background=white, anchor="center", justify="center", wraplength=720)
        self.fc_sub1 = ttk.Label(inner, background=white, anchor="center", justify="center", wraplength=720)
        self.fc_sub2 = ttk.Label(inner, background=white, anchor="center", justify="center", wraplength=720)
        self.fc_hint = ttk.Label(inner, background=white, foreground="#98a2ae", anchor="center")
        self.fc_main.pack(pady=8)
        self.fc_sub1.pack(pady=4)
        self.fc_sub2.pack(pady=4)
        self.fc_hint.pack(pady=(18, 0))
        for wdg in (self.card, inner, self.fc_main, self.fc_sub1, self.fc_sub2, self.fc_hint):
            wdg.bind("<Button-1>", lambda e: self.flip())

        bar = ttk.Frame(parent)
        bar.pack(fill="x")
        ttk.Button(bar, text="◀  Trước", command=lambda: self.goto(self.fidx - 1)).pack(side="left", expand=True, fill="x", padx=4)
        ttk.Button(bar, text="Lật thẻ  (Space)", command=self.flip).pack(side="left", expand=True, fill="x", padx=4)
        ttk.Button(bar, text="Sau  ▶", command=lambda: self.goto(self.fidx + 1)).pack(side="left", expand=True, fill="x", padx=4)
        ttk.Label(parent, foreground=GREY, text="Phím tắt: ← → chuyển thẻ,  Space lật thẻ").pack(anchor="w", pady=(6, 0))

    def reset_deck(self):
        if not hasattr(self, "fc_main"):
            return
        self.deck = self.selected_words()
        self.goto(0)

    def shuffle_deck(self):
        random.shuffle(self.deck)
        self.goto(0)

    def pick_front(self, w):
        m = FRONT_MAP[self.fc_front.get()]
        return random.choice(list(w.fields())) if m == "rand" else m

    def goto(self, i):
        if self.deck:
            self.fidx = i % len(self.deck)
            self.cur_front = self.pick_front(self.deck[self.fidx])
        self.flipped = False
        self.render_card()

    def flip(self):
        if self.deck:
            self.flipped = not self.flipped
            self.render_card()

    def render_card(self):
        if not self.deck:
            self.fc_main.config(text="Chưa chọn bài nào", font=(self.VN, 22))
            self.fc_sub1.config(text="")
            self.fc_sub2.config(text="")
            self.fc_hint.config(text="")
            self.fc_counter.config(text="0 / 0")
            return
        w = self.deck[self.fidx]
        self.fc_counter.config(text=f"{self.fidx + 1} / {len(self.deck)}   ·   第{w.lesson}課")
        if not self.flipped:
            f = self.cur_front
            self.fc_main.config(text=w.get(f), font=self.font(f, 44 if f != "vi" else 28, True))
            self.fc_sub1.config(text="")
            self.fc_sub2.config(text="")
            self.fc_hint.config(text="(nhấn vào thẻ hoặc Space để lật)")
        else:
            self.fc_main.config(text=w.w, font=self.font("kanji", 44, True))
            self.fc_sub1.config(text=w.r if w.r != w.w else "", font=self.font("hira", 26))
            self.fc_sub2.config(text=w.vi, font=self.font("vi", 20), foreground=GREEN)
            self.fc_hint.config(text="")

    def flash_key(self, d):
        if self.nb.index("current") != 1:
            return
        if d == 0:
            self.flip()
        else:
            self.goto(self.fidx + d)

    # ================================================================== TEST TAB
    def build_test_tab(self, parent):
        self.setup_frame = ttk.Frame(parent)
        self.quiz_frame = ttk.Frame(parent)
        self.result_frame = ttk.Frame(parent)
        self.build_setup_ui()
        self.build_quiz_ui()
        self.build_result_ui()
        self.questions, self.qi, self.score, self.done = [], 0, 0, 0
        self.wrong, self.answered, self.cur = [], False, None
        self.show_frame(self.setup_frame)

    def show_frame(self, fr):
        for f in (self.setup_frame, self.quiz_frame, self.result_frame):
            f.pack_forget()
        fr.pack(fill="both", expand=True)

    # ---------------- setup
    def build_setup_ui(self):
        f = self.setup_frame
        ttk.Label(f, text="Thiết lập bài kiểm tra", font=(self.VN, 15, "bold")).pack(anchor="w", pady=(0, 10))
        row = ttk.Frame(f)
        row.pack(fill="x")
        self.q_vars = {k: tk.BooleanVar(value=True) for k in ("vi", "hira", "kanji")}
        self.a_vars = {k: tk.BooleanVar(value=True) for k in ("vi", "hira", "kanji")}
        lf1 = ttk.LabelFrame(row, text="Đề bài cho sẵn (hỏi về)", padding=10)
        lf1.pack(side="left", fill="both", expand=True, padx=(0, 8))
        lf2 = ttk.LabelFrame(row, text="Bạn cần trả lời (đáp)", padding=10)
        lf2.pack(side="left", fill="both", expand=True, padx=(8, 0))
        for k in ("kanji", "hira", "vi"):
            ttk.Checkbutton(lf1, text=FIELD_LABEL[k], variable=self.q_vars[k]).pack(anchor="w", pady=2)
            ttk.Checkbutton(lf2, text=FIELD_LABEL[k], variable=self.a_vars[k]).pack(anchor="w", pady=2)
        ttk.Label(f, foreground=GREY, wraplength=760,
                  text="Mỗi câu hỏi sẽ chọn ngẫu nhiên một cặp (đề → đáp) hợp lệ trong các mục bạn tick. "
                       "Ví dụ chỉ tick Kanji ở “Đề bài” và Hiragana ở “Đáp” để luyện đọc Kanji. "
                       "Câu hỏi có Kanji chỉ dùng cho các từ có chứa chữ Hán.").pack(anchor="w", pady=8)

        lf3 = ttk.LabelFrame(f, text="Hình thức trả lời", padding=10)
        lf3.pack(fill="x", pady=6)
        self.mode_var = tk.StringVar(value="type")
        ttk.Radiobutton(lf3, text="Gõ đáp án (cần bật bộ gõ tiếng Nhật cho Hiragana / Kanji; "
                                  "nghĩa tiếng Việt gõ có hoặc không dấu đều được)",
                        variable=self.mode_var, value="type").pack(anchor="w", pady=2)
        ttk.Radiobutton(lf3, text="Trắc nghiệm 4 đáp án (phím 1-4 để chọn)",
                        variable=self.mode_var, value="mc").pack(anchor="w", pady=2)

        r2 = ttk.Frame(f)
        r2.pack(fill="x", pady=10)
        ttk.Label(r2, text="Số câu:").pack(side="left")
        self.n_var = tk.StringVar(value="20")
        ttk.Spinbox(r2, from_=5, to=500, increment=5, textvariable=self.n_var, width=6).pack(side="left", padx=6)
        self.lbl_pool = ttk.Label(r2, foreground=GREY)
        self.lbl_pool.pack(side="left", padx=14)

        ttk.Button(f, text="▶  Bắt đầu kiểm tra", command=self.start_test).pack(anchor="w", pady=14, ipadx=14, ipady=4)

    def update_pool_label(self):
        if hasattr(self, "lbl_pool"):
            n = len([w for w in self.selected_words() if w.testable])
            self.lbl_pool.config(text=f"({n} từ khả dụng trong các bài đã chọn)")

    def start_test(self, words=None):
        words = words if words is not None else [w for w in self.selected_words() if w.testable]
        qset = [k for k, v in self.q_vars.items() if v.get()]
        aset = [k for k, v in self.a_vars.items() if v.get()]
        if not words:
            messagebox.showwarning("Chưa có từ", "Hãy chọn ít nhất một bài ở cột bên trái.")
            return
        if not qset or not aset:
            messagebox.showwarning("Thiếu lựa chọn", "Hãy tick ít nhất một mục ở “Đề bài” và một mục ở “Đáp”.")
            return
        try:
            n = max(1, int(self.n_var.get()))
        except ValueError:
            n = 20
        qs = build_questions(words, qset, aset, n)
        if not qs:
            messagebox.showwarning("Không tạo được câu hỏi",
                                   "Các bài đã chọn không có từ phù hợp với kiểu câu hỏi này "
                                   "(ví dụ: chọn Kanji nhưng từ chỉ có Katakana/Hiragana).")
            return
        self.questions, self.qi, self.score, self.done, self.wrong = qs, 0, 0, 0, []
        self.mode = self.mode_var.get()
        self.show_frame(self.quiz_frame)
        self.show_question()

    # ---------------- quiz UI
    def build_quiz_ui(self):
        f = self.quiz_frame
        top = ttk.Frame(f)
        top.pack(fill="x")
        self.q_header = ttk.Label(top, font=(self.VN, 12, "bold"))
        self.q_header.pack(side="left")
        self.q_score = ttk.Label(top, foreground=GREEN)
        self.q_score.pack(side="left", padx=20)
        ttk.Button(top, text="Dừng & xem kết quả", command=self.stop_test).pack(side="right")
        ttk.Separator(f).pack(fill="x", pady=10)

        self.q_type = ttk.Label(f, foreground=GREY)
        self.q_type.pack(anchor="w")
        self.q_text = ttk.Label(f, wraplength=800, justify="left", anchor="w")
        self.q_text.pack(fill="x", pady=8)
        self.q_ans = ttk.Label(f, foreground=GREY)
        self.q_ans.pack(anchor="w", pady=(14, 4))

        self.answer_area = ttk.Frame(f)
        self.answer_area.pack(fill="x")
        self.type_row = ttk.Frame(self.answer_area)
        self.entry = ttk.Entry(self.type_row, width=40)
        self.entry.pack(side="left", fill="x", expand=True)
        self.btn_check = ttk.Button(self.type_row, text="Kiểm tra (Enter)", command=self.check_typed)
        self.btn_check.pack(side="left", padx=8)
        self.mc_frame = ttk.Frame(self.answer_area)

        self.fb = ttk.Label(f, wraplength=800, justify="left", font=(self.VN, 13, "bold"))
        self.fb.pack(anchor="w", pady=(14, 4))
        self.info = ttk.Frame(f)
        self.info_w = ttk.Label(self.info, font=self.font("kanji", 20, True))
        self.info_r = ttk.Label(self.info, font=self.font("hira", 14))
        self.info_vi = ttk.Label(self.info, font=self.font("vi", 13), wraplength=800, justify="left")
        self.info_w.pack(anchor="w")
        self.info_r.pack(anchor="w")
        self.info_vi.pack(anchor="w")
        self.act = ttk.Frame(f)
        self.btn_override = ttk.Button(self.act, text="Tính là đúng", command=self.override_correct)
        self.btn_next = ttk.Button(self.act, text="Câu tiếp ▶  (Enter)", command=self.next_question)
        self.btn_next.pack(side="right")

    def accepted_texts(self, wd, s, t):
        return {x.get(t) for x in self.index[s].get(wd.get(s), [wd]) if t in x.fields()} | {wd.get(t)}

    def show_question(self):
        wd, s, t = self.questions[self.qi]
        self.cur = (wd, s, t)
        self.answered = False
        self.cur_wrong_entry = None
        self.q_header.config(text=f"Câu {self.qi + 1} / {len(self.questions)}")
        self.q_score.config(text=f"Đúng: {self.score}")
        self.q_type.config(text=f"Đề bài — {FIELD_LABEL[s]}")
        self.q_text.config(text=wd.get(s), font=self.font(s, 34 if s != "vi" else 22, True))
        hint = {"hira": "Hiragana", "kanji": "Kanji / chữ viết", "vi": "Nghĩa tiếng Việt"}[t]
        verb = "Gõ" if self.mode == "type" else "Chọn"
        self.q_ans.config(text=f"{verb} đáp án — {hint}:")
        self.fb.config(text="")
        self.info.pack_forget()
        self.act.pack_forget()
        self.btn_override.pack_forget()

        for ch in self.mc_frame.winfo_children():
            ch.destroy()
        self.type_row.pack_forget()
        self.mc_frame.pack_forget()
        if self.mode == "type":
            self.type_row.pack(fill="x")
            self.entry.config(state="normal", font=self.font(t, 18))
            self.entry.delete(0, "end")
            self.btn_check.config(state="normal")
            self.entry.focus_set()
        else:
            self.mc_frame.pack(fill="x")
            self.opts = self.make_options(wd, s, t)
            self.mc_buttons = []
            for i, opt in enumerate(self.opts):
                b = tk.Button(self.mc_frame, text=f"{'ABCD'[i]}.  {opt}", anchor="w", justify="left",
                              wraplength=760, font=self.font(t, 14), relief="groove", padx=10, pady=6,
                              command=lambda k=i: self.pick_option(k))
                b.pack(fill="x", pady=3)
                self.mc_buttons.append(b)

    def make_options(self, wd, s, t):
        ok = self.accepted_texts(wd, s, t)
        correct = wd.get(t)
        pool = list({x.get(t) for x in WORDS if t in x.fields() and x.get(t) not in ok})
        near = [p for p in pool if abs(len(p) - len(correct)) <= 3]
        cand = near if len(near) >= 3 else pool
        opts = random.sample(cand, min(3, len(cand))) + [correct]
        random.shuffle(opts)
        return opts

    # ---------------- answering
    def check_typed(self):
        if self.answered:
            return
        wd, s, t = self.cur
        user = self.entry.get()
        if not user.strip():
            return
        accepted = self.accepted_texts(wd, s, t)
        if t == "vi":
            ok = any(meaning_ok(user, a) for a in accepted)
        elif t == "hira":
            u = norm_jp(user, hira=True)
            ok = any(u == norm_jp(a, hira=True) for a in accepted)
        else:
            u = norm_jp(user)
            ok = any(u == norm_jp(a) for a in accepted)
        self.entry.config(state="disabled")
        self.btn_check.config(state="disabled")
        self.finish_answer(ok)

    def pick_option(self, k):
        if self.answered:
            return
        wd, s, t = self.cur
        accepted = self.accepted_texts(wd, s, t)
        for i, b in enumerate(self.mc_buttons):
            b.config(state="disabled")
            if self.opts[i] in accepted:
                b.config(bg="#c8f0d2", disabledforeground="#000000")
        ok = self.opts[k] in accepted
        if not ok:
            self.mc_buttons[k].config(bg="#f5c6c0", disabledforeground="#000000")
        self.finish_answer(ok)

    def finish_answer(self, ok):
        wd, s, t = self.cur
        self.answered = True
        self.done += 1
        if ok:
            self.score += 1
            self.fb.config(text="✔  Chính xác!", foreground=GREEN)
        else:
            self.cur_wrong_entry = (wd, s, t)
            self.wrong.append(self.cur_wrong_entry)
            self.fb.config(text=f"✘  Chưa đúng.  Đáp án: {wd.get(t)}", foreground=RED)
            self.btn_override.pack(side="right", padx=8)
        self.q_score.config(text=f"Đúng: {self.score}")
        self.info_w.config(text=wd.w)
        self.info_r.config(text=wd.r if wd.r != wd.w else "")
        self.info_vi.config(text=wd.vi)
        self.info.pack(anchor="w", pady=8)
        self.act.pack(fill="x", pady=8)

    def override_correct(self):
        if self.cur_wrong_entry and self.cur_wrong_entry in self.wrong:
            self.wrong.remove(self.cur_wrong_entry)
            self.cur_wrong_entry = None
            self.score += 1
            self.q_score.config(text=f"Đúng: {self.score}")
            self.fb.config(text="✔  Đã tính là đúng.", foreground=GREEN)
            self.btn_override.pack_forget()

    def next_question(self):
        self.qi += 1
        if self.qi >= len(self.questions):
            self.finish_test()
        else:
            self.show_question()

    def stop_test(self):
        if self.done == 0 or messagebox.askyesno("Dừng kiểm tra", "Dừng và xem kết quả với các câu đã làm?"):
            self.finish_test()

    def on_return(self, e=None):
        if self.nb.index("current") != 2 or not self.quiz_frame.winfo_ismapped():
            return
        if self.answered:
            self.next_question()
        elif self.mode == "type":
            self.check_typed()

    def on_number(self, k):
        if (self.nb.index("current") == 2 and self.quiz_frame.winfo_ismapped()
                and self.mode == "mc" and not self.answered and k < len(self.opts)):
            self.pick_option(k)

    # ---------------- results
    def build_result_ui(self):
        f = self.result_frame
        self.res_title = ttk.Label(f, font=(self.VN, 18, "bold"))
        self.res_title.pack(anchor="w", pady=(0, 4))
        self.res_sub = ttk.Label(f, foreground=GREY)
        self.res_sub.pack(anchor="w", pady=(0, 10))
        ttk.Label(f, text="Các từ làm sai / chưa nhớ:", font=(self.VN, 11, "bold")).pack(anchor="w")
        box = ttk.Frame(f)
        box.pack(fill="both", expand=True, pady=6)
        self.res_tree = ttk.Treeview(box, columns=("w", "r", "vi"), show="headings")
        for c, text, wd in (("w", "Kanji / chữ viết", 220), ("r", "Hiragana", 240), ("vi", "Nghĩa", 380)):
            self.res_tree.heading(c, text=text)
            self.res_tree.column(c, width=wd, anchor="w")
        sb = ttk.Scrollbar(box, orient="vertical", command=self.res_tree.yview)
        self.res_tree.configure(yscrollcommand=sb.set)
        self.res_tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        bar = ttk.Frame(f)
        bar.pack(fill="x", pady=6)
        self.btn_retry = ttk.Button(bar, text="🔁  Làm lại các từ sai", command=self.retry_wrong)
        self.btn_retry.pack(side="left", padx=(0, 8))
        ttk.Button(bar, text="⚙  Quay lại thiết lập", command=lambda: self.show_frame(self.setup_frame)).pack(side="left")

    def finish_test(self):
        total = max(self.done, 1)
        pct = round(100 * self.score / total)
        self.res_title.config(text=f"Kết quả: {self.score} / {self.done}  ({pct}%)")
        self.res_sub.config(text="Tuyệt vời!" if pct >= 90 else "Khá tốt, ôn thêm vài từ nữa nhé." if pct >= 60
                            else "Cố gắng thêm nào, thử làm lại các từ sai!")
        self.res_tree.delete(*self.res_tree.get_children())
        seen = set()
        for wd, s, t in self.wrong:
            if id(wd) in seen:
                continue
            seen.add(id(wd))
            self.res_tree.insert("", "end", values=(wd.w, wd.r, wd.vi))
        self.btn_retry.config(state="normal" if self.wrong else "disabled")
        self.show_frame(self.result_frame)

    def retry_wrong(self):
        words = []
        for wd, s, t in self.wrong:
            if wd not in words:
                words.append(wd)
        self.n_var.set(str(max(len(words), 1)))
        self.start_test(words)


if __name__ == "__main__":
    App().mainloop()

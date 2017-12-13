# coding=utf-8
import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait


def isElementExist(element, driver):
    flag = True

    try:
        driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag


# soup = BeautifulSoup(open('linkedin_list.html'), "html.parser")
# r = soup.find_all('a',class_='mn-person-info__picture ember-view')
# url = []
# for i in r:
#     # print i
#     # print i['href']
#     url.append('http://www.linkedin.com'+i['href'])
'''
jxm@hfm-phe.com            23957648jxm

https://www.linkedin.com/mynetwork/invite-connect/connections/
mary@hfm-phe.com           zq3856523

hao_monica@sina.com        monicafeng1990
eva@hfm-phe.com            229911zzy!
'''
username = raw_input("please input your username: ")  # input 函数的使用
password = raw_input("please input your password: ")  # input 函数的使用
time.sleep(5)
url_list = [u'http://www.linkedin.com/in/stevan-petkovic-54004065/',
            u'http://www.linkedin.com/in/capt-joginder-singh-dhanda-37985a56/',
            u'http://www.linkedin.com/in/prasanth-sankaranarayanan-b9b5b417/',
            u'http://www.linkedin.com/in/demetra-demetriou-9b65ba60/',
            u'http://www.linkedin.com/in/mario-friedrich-b2b103b8/',
            u'http://www.linkedin.com/in/anthony-zou-53a67088/',
            u'http://www.linkedin.com/in/md-jahidul-islam-9b65a346/',
            u'http://www.linkedin.com/in/deepak-patil-43556661/',
            u'http://www.linkedin.com/in/ship-chandler-equatorial-guinea-736bb6b0/',
            u'http://www.linkedin.com/in/raja-sekhar-boni-1a966b91/',
            u'http://www.linkedin.com/in/my-quyen-mary-pham-45595037/',
            u'http://www.linkedin.com/in/basem-alfar-b405b238/',
            u'http://www.linkedin.com/in/bent-olesen-05004892/',
            u'http://www.linkedin.com/in/shinyayoshikawa/',
            u'http://www.linkedin.com/in/loisa-ang-06833b31/',
            u'http://www.linkedin.com/in/abdul-rasheed-kareem-a23b5834/',
            u'http://www.linkedin.com/in/john-roddy-98309139/',
            u'http://www.linkedin.com/in/roberto-colombo-95a3613b/',
            u'http://www.linkedin.com/in/vignesh-j-5bb6634b/',
            u'http://www.linkedin.com/in/navin-a-b88206113/',
            u'http://www.linkedin.com/in/m-raaj-kumar-a8018575/',
            u'http://www.linkedin.com/in/syed-burhan-globus-international-marine-india-and-singapore-95046b57/',
            u'http://www.linkedin.com/in/crystal-zhai-b28034131/',
            u'http://www.linkedin.com/in/sapmarkgonzales21/',
            u'http://www.linkedin.com/in/jeff-huang-48a831140/',
            u'http://www.linkedin.com/in/roman-romejko-626b1186/',
            u'http://www.linkedin.com/in/petrosan-daniel-madalin-78a57b13/',
            u'http://www.linkedin.com/in/muhammad-alamgir-bb67a333/',
            u'http://www.linkedin.com/in/emre-uyanik-74077570/',
            u'http://www.linkedin.com/in/kaan-r-bektas-629573103/',
            u'http://www.linkedin.com/in/rached-briki-ba644b56/',
            u'http://www.linkedin.com/in/jignesh-shah-65446114/',
            u'http://www.linkedin.com/in/tolga-biren-b817a326/',
            u'http://www.linkedin.com/in/abdelghani-harfi-5b8b8018/',
            u'http://www.linkedin.com/in/radhiah-sulaiman-a00a3b39/',
            u'http://www.linkedin.com/in/riccardo-masiero-242b7848/',
            u'http://www.linkedin.com/in/peter-fr%C3%B6mming-24598162/',
            u'http://www.linkedin.com/in/abdul-nazir-batingkay-b53bb15a/',
            u'http://www.linkedin.com/in/pepebris/',
            u'http://www.linkedin.com/in/syam-nair-b4ba0b68/',
            u'http://www.linkedin.com/in/karenrhodes2015/',
            u'http://www.linkedin.com/in/socrates-pilavakis-2307ba61/',
            u'http://www.linkedin.com/in/paolo-carpaneto-464854b/',
            u'http://www.linkedin.com/in/jack-sharif-5b09abb0/',
            u'http://www.linkedin.com/in/barla-sai-kumar-148939b6/',
            u'http://www.linkedin.com/in/vikash-singh-43915a37/',
            u'http://www.linkedin.com/in/amit-dey-b5454518/',
            u'http://www.linkedin.com/in/robert-zhang-2399781b/',
            u'http://www.linkedin.com/in/jack-wei-b30b3480/',
            u'http://www.linkedin.com/in/joko-mardianto-a8789b111/',
            u'http://www.linkedin.com/in/imran-hussain-96b28151/',
            u'http://www.linkedin.com/in/david-yu-9301933a/',
            u'http://www.linkedin.com/in/benoelectric/',
            u'http://www.linkedin.com/in/muhammad-yakoob-24a77ba/',
            u'http://www.linkedin.com/in/majestic-marine-and-engineering-services-5a0715134/',
            u'http://www.linkedin.com/in/desmondaubery/',
            u'http://www.linkedin.com/in/william-snedigar-8b3522106/',
            u'http://www.linkedin.com/in/jonathan-t-dean-674406141/',
            u'http://www.linkedin.com/in/omay-omay-323002109/',
            u'http://www.linkedin.com/in/eray-baydar-86b940b4/',
            u'http://www.linkedin.com/in/kolhatkar-bhalchandra-4415677b/',
            u'http://www.linkedin.com/in/glxc-alice/',
            u'http://www.linkedin.com/in/sudhi-jose-089483b3/',
            u'http://www.linkedin.com/in/virendrasinh-parmar-3837a763/',
            u'http://www.linkedin.com/in/sayiner/',
            u'http://www.linkedin.com/in/greg-lauderdale-8794b72b/',
            u'http://www.linkedin.com/in/jason-zhang-a84741144/',
            u'http://www.linkedin.com/in/king-new-a10333112/',
            u'http://www.linkedin.com/in/jeremy-friesland-5202a4111/',
            u'http://www.linkedin.com/in/zeng-vicky-ba0368b9/',
            u'http://www.linkedin.com/in/joshrees1/',
            u'http://www.linkedin.com/in/%E5%B0%BC%E5%B0%94-%E4%B8%B9-525b43142/',
            u'http://www.linkedin.com/in/seana-cho-8265a0129/',
            u'http://www.linkedin.com/in/justin-jia-22890113b/',
            u'http://www.linkedin.com/in/yong-huang-43247ab9/',
            u'http://www.linkedin.com/in/%E4%B8%96%E6%B0%91-%E9%99%88-88b78413b/',
            u'http://www.linkedin.com/in/%E4%BF%9E-%E5%BC%A0-96a658131/',
            u'http://www.linkedin.com/in/emre-k%C3%BC%C3%A7%C3%BCkaky%C3%BCz-396b7810b/',
            u'http://www.linkedin.com/in/murugesan-kandasamy-04666722/',
            u'http://www.linkedin.com/in/marissa-manrique-garcia-y-lanz-25738689/',
            u'http://www.linkedin.com/in/yogeshkhairnar/',
            u'http://www.linkedin.com/in/%E5%BB%BA%E7%94%9F-%E5%BC%A0-b7378997/',
            u'http://www.linkedin.com/in/robert-russell-4433a2a0/',
            u'http://www.linkedin.com/in/jafari-ali/',
            u'http://www.linkedin.com/in/jeet-makadia-6b1a63124/',
            u'http://www.linkedin.com/in/sharon-packham-2bb248a4/',
            u'http://www.linkedin.com/in/plate-heat-exchanger/',
            u'http://www.linkedin.com/in/anders-valeskog-6149a116/',
            u'http://www.linkedin.com/in/ahryung-jin-b5241ab0/',
            u'http://www.linkedin.com/in/sealordinsulation-insulation-398986b8/',
            u'http://www.linkedin.com/in/joletta-zhao-4294ab135/',
            u'http://www.linkedin.com/in/chetan-shah-679a86a9/',
            u'http://www.linkedin.com/in/karina-grubert-ab04b498/',
            u'http://www.linkedin.com/in/mary-yan-4a3a5698/',
            u'http://www.linkedin.com/in/kishore-isapure-788142137/',
            u'http://www.linkedin.com/in/igor-durcansky-62851a2a/',
            u'http://www.linkedin.com/in/miriam-rodway-94122616/',
            u'http://www.linkedin.com/in/mark-kenyon-8638b419/',
            u'http://www.linkedin.com/in/%E6%88%90%E9%BE%99-%E9%A9%AC-846730135/',
            u'http://www.linkedin.com/in/vivek-pathak-6240349a/',
            u'http://www.linkedin.com/in/liana-vetere-2415487a/',
            u'http://www.linkedin.com/in/sebastiano-di-lena-5844b941/',
            u'http://www.linkedin.com/in/lyman-tu-64bab5a/',
            u'http://www.linkedin.com/in/lliew-evonne-0309302b/',
            u'http://www.linkedin.com/in/riju-vasal-85b96964/',
            u'http://www.linkedin.com/in/scott-riddell-b65369a5/',
            u'http://www.linkedin.com/in/asfaque-ali-669980ab/',
            u'http://www.linkedin.com/in/chloecraigen14/',
            u'http://www.linkedin.com/in/vinay-chowdary-a03253a4/',
            u'http://www.linkedin.com/in/tom-ryan-a9791127/',
            u'http://www.linkedin.com/in/harald-hoogendoorn-8090805/',
            u'http://www.linkedin.com/in/emmanuel-hoffmann-93066b1/',
            u'http://www.linkedin.com/in/sotto-zero-62a58476/',
            u'http://www.linkedin.com/in/rina-kaur-61a19992/',
            u'http://www.linkedin.com/in/sandra-van-dijk-834867aa/',
            u'http://www.linkedin.com/in/stefanlm-eriksson-gm/',
            u'http://www.linkedin.com/in/vaisakh-k-7b411a8b/',
            u'http://www.linkedin.com/in/nikolaostheocharis/',
            u'http://www.linkedin.com/in/bill-kearley-19186781/',
            u'http://www.linkedin.com/in/michael-siebmann-69237917/',
            u'http://www.linkedin.com/in/%E5%AE%B6%E7%87%95-%E5%91%A8-5082a6134/',
            u'http://www.linkedin.com/in/gwyn-taylor-b15a8178/',
            u'http://www.linkedin.com/in/ricki-nagra-92493747/',
            u'http://www.linkedin.com/in/murat-kili%C3%A7-klc-so%C4%9Futma-66869341/',
            u'http://www.linkedin.com/in/thomas-wastell-55b33641/',
            u'http://www.linkedin.com/in/chris-edwards-5bab9098/',
            u'http://www.linkedin.com/in/russellborg/',
            u'http://www.linkedin.com/in/willem-witjes-a5435586/',
            u'http://www.linkedin.com/in/lilly-jin-b5b33b28/',
            u'http://www.linkedin.com/in/betosaes/',
            u'http://www.linkedin.com/in/davidedemola/',
            u'http://www.linkedin.com/in/luke-bithell-7b1299132/',
            u'http://www.linkedin.com/in/danny-woodin-b9248910a/',
            u'http://www.linkedin.com/in/srikanth-gollavilli-09297542/',
            u'http://www.linkedin.com/in/james-bell-28458a34/',
            u'http://www.linkedin.com/in/sonia-vazquez-1116b332/',
            u'http://www.linkedin.com/in/thitabadh-nidhijotibhurinath-14344b69/',
            u'http://www.linkedin.com/in/david-whittingham-19205529/',
            u'http://www.linkedin.com/in/sarah-woolley-95781b5a/',
            u'http://www.linkedin.com/in/chris-lian-07a83712b/',
            u'http://www.linkedin.com/in/shailendra-deshpande-15980118/',
            u'http://www.linkedin.com/in/echo-du-471aa2b9/',
            u'http://www.linkedin.com/in/megan-mata-25b7a640/',
            u'http://www.linkedin.com/in/saphex-heat-exchangers-37952b101/',
            u'http://www.linkedin.com/in/v-subramanian-3b5b1a79/',
            u'http://www.linkedin.com/in/sophia-xiao-886300136/',
            u'http://www.linkedin.com/in/vijay-bodke-2a435635/',
            u'http://www.linkedin.com/in/supaluck-poonsakul-ba2858a5/',
            u'http://www.linkedin.com/in/james-liss-6b4a2285/',
            u'http://www.linkedin.com/in/shm-safety-5548a5106/',
            u'http://www.linkedin.com/in/berendjan-sloot-b486366/',
            u'http://www.linkedin.com/in/karthik-nagarajan-72b58b97/',
            u'http://www.linkedin.com/in/g%C3%B6ran-fokuhl-04303329/',
            u'http://www.linkedin.com/in/mark-richardson-56a18356/',
            u'http://www.linkedin.com/in/vincent-sylvester-pinto-81533047/',
            u'http://www.linkedin.com/in/stewart-henderson-33705b48/',
            u'http://www.linkedin.com/in/huriye-ayd%C4%B1n-97235265/',
            u'http://www.linkedin.com/in/anchor-ship-chandlers-823ba8100/',
            u'http://www.linkedin.com/in/ken-chan-97267093/',
            u'http://www.linkedin.com/in/john-cornelissen-272b64a3/',
            u'http://www.linkedin.com/in/vijay-shivaji-patil-92552810a/',
            u'http://www.linkedin.com/in/ashutosh-dixit-6a01b624/',
            u'http://www.linkedin.com/in/tinsana-duckmanton-332a64bb/',
            u'http://www.linkedin.com/in/shiraz-khan-50254220/',
            u'http://www.linkedin.com/in/arialdo-giammusso-0698a532/',
            u'http://www.linkedin.com/in/henrik-thomsen-08377967/',
            u'http://www.linkedin.com/in/ahmed-hussein-345894a5/',
            u'http://www.linkedin.com/in/fabio-fogliani-363270133/',
            u'http://www.linkedin.com/in/dejan-trajkovic-3b5208ab/',
            u'http://www.linkedin.com/in/alfonso-thawe-671922b/',
            u'http://www.linkedin.com/in/cristiani-milan-ferreira-45a17b42/',
            u'http://www.linkedin.com/in/santosh-patil-3389b740/',
            u'http://www.linkedin.com/in/asiandave/',
            u'http://www.linkedin.com/in/manwarf-cheng-b4ba5a49/',
            u'http://www.linkedin.com/in/jaya-uttam-69506529/',
            u'http://www.linkedin.com/in/pierre-chaix-a5007261/',
            u'http://www.linkedin.com/in/vivek-dharmadhikari-615a0b12a/',
            u'http://www.linkedin.com/in/jesper-olsen-68500417/',
            u'http://www.linkedin.com/in/vijaymali/',
            u'http://www.linkedin.com/in/matthew-moore-bsc-hons-bb31732a/',
            u'http://www.linkedin.com/in/sayeed-tayyabi-a81b71a8/',
            u'http://www.linkedin.com/in/tingting-zhu-023421132/',
            u'http://www.linkedin.com/in/junaid-mateen-1063b993/',
            u'http://www.linkedin.com/in/scott-cameron-2b2402b5/',
            u'http://www.linkedin.com/in/mahdi-bahari-27839468/',
            u'http://www.linkedin.com/in/mukesh-shukla-b7909040/',
            u'http://www.linkedin.com/in/michele-librandi-8241872a/',
            u'http://www.linkedin.com/in/vincent-d-2689424a/',
            u'http://www.linkedin.com/in/waleed-al-hisnawy-16a90057/',
            u'http://www.linkedin.com/in/simonbiggs/',
            u'http://www.linkedin.com/in/eglitis-gints-90976382/',
            u'http://www.linkedin.com/in/tor-fredrik-skoie-6a9a372a/',
            u'http://www.linkedin.com/in/gurunath-borkar-0b15ab10/',
            u'http://www.linkedin.com/in/jitender-ghanghas-8177331a/',
            u'http://www.linkedin.com/in/lorenzo-bagante-9bb9265/',
            u'http://www.linkedin.com/in/arthur-sandum-30218655/',
            u'http://www.linkedin.com/in/mathieu-breton-84088265/',
            u'http://www.linkedin.com/in/richard-hodgson-5b7031101/',
            u'http://www.linkedin.com/in/anna-schmiegel-72505186/',
            u'http://www.linkedin.com/in/alaska-so%C4%9Futma-a%C5%9F-refrigeration-ltd-co-24630347/',
            u'http://www.linkedin.com/in/roberto-russo-394b1424/',
            u'http://www.linkedin.com/in/fernandogarciamateos/',
            u'http://www.linkedin.com/in/tony-elsdon-3410824b/',
            u'http://www.linkedin.com/in/robert-patrick-92646851/',
            u'http://www.linkedin.com/in/herman-verbeek-27b93370/',
            u'http://www.linkedin.com/in/laura-pelizzoli-98314139/',
            u'http://www.linkedin.com/in/andrei-baciu-a246786a/',
            u'http://www.linkedin.com/in/valeria-assandri-b71496a8/',
            u'http://www.linkedin.com/in/galenopietrorossato/',
            u'http://www.linkedin.com/in/stefan-mitrov-b16b736b/',
            u'http://www.linkedin.com/in/cristiano-negri-ba903836/',
            u'http://www.linkedin.com/in/david-norris-49599a25/',
            u'http://www.linkedin.com/in/jeff-liu-27789572/',
            u'http://www.linkedin.com/in/henrik-bruun/',
            u'http://www.linkedin.com/in/emilie-stouthandel-227b6288/',
            u'http://www.linkedin.com/in/daniele-vaccarini-3300b138/',
            u'http://www.linkedin.com/in/andrea-paolo-giorgi-36521724/',
            u'http://www.linkedin.com/in/giacomocostagli/',
            u'http://www.linkedin.com/in/piyush-sharma-21966015/',
            u'http://www.linkedin.com/in/arunkumarbhatia/',
            u'http://www.linkedin.com/in/archi-monyleak-leak-09038a125/',
            u'http://www.linkedin.com/in/vagnhaagenpetersen/',
            u'http://www.linkedin.com/in/kanokwan-khamkong-202217b3/',
            u'http://www.linkedin.com/in/john-miao-b1786875/',
            u'http://www.linkedin.com/in/ben-parasram-48360022/',
            u'http://www.linkedin.com/in/amit-yadav-75a46721/',
            u'http://www.linkedin.com/in/ozgur-firat-demir-9698bb88/',
            u'http://www.linkedin.com/in/mertekinozkan/',
            u'http://www.linkedin.com/in/celery-liu-96810a123/',
            u'http://www.linkedin.com/in/chad-bishop-81834157/',
            u'http://www.linkedin.com/in/blair-zhang-088089117/',
            u'http://www.linkedin.com/in/tylan-lambert-2b979296/',
            u'http://www.linkedin.com/in/blue-seaservices-india-b181b24b/',
            u'http://www.linkedin.com/in/athena-shi-153233a4/',
            u'http://www.linkedin.com/in/kay-pei-421087117/',
            u'http://www.linkedin.com/in/%E4%B9%94%E5%AD%90-%E6%9D%A8-924a39109/',
            u'http://www.linkedin.com/in/nicole-marceaux-736668121/',
            u'http://www.linkedin.com/in/vimal-shah-0407669b/',
            u'http://www.linkedin.com/in/katherine-sundt-a42311119/',
            u'http://www.linkedin.com/in/%E8%BE%B0-%E8%BF%88-b060a5135/',
            u'http://www.linkedin.com/in/rabienaamani/',
            u'http://www.linkedin.com/in/sujit-potdar-4999744/',
            u'http://www.linkedin.com/in/mikkel-gytz-olesen-5a07a2a7/',
            u'http://www.linkedin.com/in/ayhan-durak-9a03409b/',
            u'http://www.linkedin.com/in/%E4%BA%89%E4%BC%9F-%E7%8E%8B-316773134/',
            u'http://www.linkedin.com/in/ravi-jagtap-19324475/',
            u'http://www.linkedin.com/in/o%C4%9Fuz-ata%C3%A7-69698980/',
            u'http://www.linkedin.com/in/diana-z-b0a4a5119/',
            u'http://www.linkedin.com/in/pritesh-makwana-70619922/',
            u'http://www.linkedin.com/in/kashif-ali-a01a1a2a/',
            u'http://www.linkedin.com/in/umaar-bin-suhail-2b649427/',
            u'http://www.linkedin.com/in/atul-upadhyay-11116420/',
            u'http://www.linkedin.com/in/annsorensen/',
            u'http://www.linkedin.com/in/andrealascala/',
            u'http://www.linkedin.com/in/christian-schweier-8263537a/',
            u'http://www.linkedin.com/in/p-v-b-pumps-p-kirk-34a455115/',
            u'http://www.linkedin.com/in/hanne-kronborg-7a252513/',
            u'http://www.linkedin.com/in/umer-muneer-chudhary-ieng-mimeche-67782063/',
            u'http://www.linkedin.com/in/vicky-zhang-155965133/',
            u'http://www.linkedin.com/in/cherry-ann-r-mendevil-3305b524/',
            u'http://www.linkedin.com/in/%E7%AB%8B%E4%B8%9C-%E5%B4%94-052657132/',
            u'http://www.linkedin.com/in/stefan-rydh-38724263/',
            u'http://www.linkedin.com/in/karl-johan-sveningsson-33736b57/',
            u'http://www.linkedin.com/in/cherry-han-099657132/',
            u'http://www.linkedin.com/in/helle-frandsen-76913b68/',
            u'http://www.linkedin.com/in/hamid-ali-b9406290/',
            u'http://www.linkedin.com/in/richie-pius-994b9768/',
            u'http://www.linkedin.com/in/%E6%88%90-%E8%8C%83-539916132/',
            u'http://www.linkedin.com/in/michel-van-noort-4a51281b/',
            u'http://www.linkedin.com/in/joe-gao-254656132/',
            u'http://www.linkedin.com/in/bivash-sunder-patel-2a622037/',
            u'http://www.linkedin.com/in/%E6%89%BF%E7%91%9C-%E6%9D%8E-a2291b132/',
            u'http://www.linkedin.com/in/minaz-ravjani-68353812a/',
            u'http://www.linkedin.com/in/%E5%B8%8C%E6%96%87-%E8%92%8B-75a915132/',
            u'http://www.linkedin.com/in/%E5%BB%BA%E5%BF%A0-%E9%BB%84-697664132/',
            u'http://www.linkedin.com/in/bin-ye-4278a7bb/',
            u'http://www.linkedin.com/in/paul-tsui-618657132/',
            u'http://www.linkedin.com/in/%E6%99%93%E8%BF%9E-%E7%BA%AA-090656132/',
            u'http://www.linkedin.com/in/tracy-yan-477657132/',
            u'http://www.linkedin.com/in/minnie-meng-124657132/',
            u'http://www.linkedin.com/in/byron-stewart-72206787/',
            u'http://www.linkedin.com/in/kit-lee-0165b2116/',
            u'http://www.linkedin.com/in/%E5%BF%B5-%E5%88%98-b24a2a120/',
            u'http://www.linkedin.com/in/wu-evson-76b648b4/',
            u'http://www.linkedin.com/in/villena-f-felix-6b6438122/',
            u'http://www.linkedin.com/in/german-pianesi-8ba77938/',
            u'http://www.linkedin.com/in/xxm1130/', u'http://www.linkedin.com/in/ellietao/',
            u'http://www.linkedin.com/in/muhammad-imran-8579b036/',
            u'http://www.linkedin.com/in/yao-xiaona-00240793/',
            u'http://www.linkedin.com/in/kaj-rissler-2a932916/',
            u'http://www.linkedin.com/in/dupeng-wang-8ba925101/',
            u'http://www.linkedin.com/in/andres-tubillas-754b005b/',
            u'http://www.linkedin.com/in/pantelis-stylianopoulos-9757803a/',
            u'http://www.linkedin.com/in/tina-liu-b42015a2/',
            u'http://www.linkedin.com/in/konstantin-kuznetsov-45a207a5/',
            u'http://www.linkedin.com/in/jenny-zhang-1170a132/',
            u'http://www.linkedin.com/in/mr-anurag-gupta-84977a5/',
            u'http://www.linkedin.com/in/seanwooo/',
            u'http://www.linkedin.com/in/%E5%BF%97%E9%BE%99-%E5%BC%A0-b94a6bb8/',
            u'http://www.linkedin.com/in/suresh-thangarasu-811319111/',
            u'http://www.linkedin.com/in/jessica-plate-heat-exchanger-0b49b2b6/',
            u'http://www.linkedin.com/in/les-jackowski-85a74728/',
            u'http://www.linkedin.com/in/willert-boevee-4b472130/',
            u'http://www.linkedin.com/in/kamilla-s%C3%B8g%C3%A5rd-poulsen-764ba86/',
            u'http://www.linkedin.com/in/phillip-everall-29941241/',
            u'http://www.linkedin.com/in/mike-zhang-5b65a137/',
            u'http://www.linkedin.com/in/sergio-medina-3a680321/',
            u'http://www.linkedin.com/in/michael-spalding-76b1719a/',
            u'http://www.linkedin.com/in/paoloconsonni/',
            u'http://www.linkedin.com/in/james-jim-carr-17b37177/',
            u'http://www.linkedin.com/in/abdennour-tamdrari-67001746/',
            u'http://www.linkedin.com/in/morten-hildebrand-3a470a6/',
            u'http://www.linkedin.com/in/cmyidea/',
            u'http://www.linkedin.com/in/grace-zhao-36217598/',
            u'http://www.linkedin.com/in/josh-maloff-4111422a/',
            u'http://www.linkedin.com/in/paul-forgang-7b4aa235/',
            u'http://www.linkedin.com/in/peter-chen-a476b9/',
            u'http://www.linkedin.com/in/elaine-wu-883a9523/',
            u'http://www.linkedin.com/in/giulio-sozzi-12a67148/',
            u'http://www.linkedin.com/in/fabiozaca/', u'http://www.linkedin.com/in/alfazmarine/',
            u'http://www.linkedin.com/in/guenther-mathe-9aa067a8/',
            u'http://www.linkedin.com/in/alexisbonhomme/',
            u'http://www.linkedin.com/in/%E9%93%B6%E5%B7%9E-%E4%BB%BB-268312108/',
            u'http://www.linkedin.com/in/christophe-zwick-9643295b/',
            u'http://www.linkedin.com/in/jian-yunfeng-64a42b20/',
            u'http://www.linkedin.com/in/tracy-hong-905595a2/',
            u'http://www.linkedin.com/in/nancy-he-a34338109/',
            u'http://www.linkedin.com/in/joy-wu-b814b9125/',
            u'http://www.linkedin.com/in/birgitte-bodin-schalech-7370b462/',
            u'http://www.linkedin.com/in/helen-han-8889a938/',
            u'http://www.linkedin.com/in/interlink-maritech-service-99564323/',
            u'http://www.linkedin.com/in/lucky-dhludhlu-4bbb0991/',
            u'http://www.linkedin.com/in/irvin-godina-a8ab3141/',
            u'http://www.linkedin.com/in/adam-forchhammer-7681405/',
            u'http://www.linkedin.com/in/douglas-bolinger-959646b/',
            u'http://www.linkedin.com/in/laxmi-kant-meena-b315b722/',
            u'http://www.linkedin.com/in/rune-sandlykke-77696132/',
            u'http://www.linkedin.com/in/robert-keen-50519987/',
            u'http://www.linkedin.com/in/stevehopper120/',
            u'http://www.linkedin.com/in/monica-feng-511a1890/',
            u'http://www.linkedin.com/in/fanny-zhou-0a898643/',
            u'http://www.linkedin.com/in/abhishek-newar-56890aa6/',
            u'http://www.linkedin.com/in/kwan-woo-lee-29930082/',
            u'http://www.linkedin.com/in/naveenmann/',
            u'http://www.linkedin.com/in/rakesh-prajapati-13b7ba17/',
            u'http://www.linkedin.com/in/charlesrwitt/',
            u'http://www.linkedin.com/in/vinay-kr-singh-81724015/',
            u'http://www.linkedin.com/in/julie-zhu-1594a7102/',
            u'http://www.linkedin.com/in/audrey-ong-27ba6478/',
            u'http://www.linkedin.com/in/tommy-wu-340b7670/',
            u'http://www.linkedin.com/in/tnt-tnt-b53b7a71/',
            u'http://www.linkedin.com/in/adekoya-lateef-33ba29a1/',
            u'http://www.linkedin.com/in/%E6%96%87%E5%A8%9F-%E8%A3%B4-52a203101/',
            u'http://www.linkedin.com/in/%E4%BA%9A%E5%B7%9D-%E7%AA%A6-0162b3101/',
            u'http://www.linkedin.com/in/%E7%BB%B4%E9%BE%99-%E5%AE%8B-642771b1/',
            u'http://www.linkedin.com/in/oilcooler/',
            u'http://www.linkedin.com/in/imam-mahmudi-phe-2416b549/',
            u'http://www.linkedin.com/in/%E7%A7%89%E6%A3%A0-%E5%AE%8B-973a5391/',
            u'http://www.linkedin.com/in/ritesh-prajapati-84a12545/',
            u'http://www.linkedin.com/in/raj-patel-7a4a2994/',
            u'http://www.linkedin.com/in/amanda-qian-751141108/',
            u'http://www.linkedin.com/in/flora-lu-51a6a5101/',
            u'http://www.linkedin.com/in/pallav-mehta-09277b50/',
            u'http://www.linkedin.com/in/dhiraj-ojha-b7985bb3/',
            u'http://www.linkedin.com/in/frank-gasiewski-96293632/',
            u'http://www.linkedin.com/in/rocoreholdings/',
            u'http://www.linkedin.com/in/alan-letele-846917a6/',
            u'http://www.linkedin.com/in/%E4%BF%8A%E5%B3%B0-%E5%88%98-4a2050b5/',
            u'http://www.linkedin.com/in/barbaros-gencer-a13ab842/',
            u'http://www.linkedin.com/in/aaron-zhang-56b26a79/',
            u'http://www.linkedin.com/in/muzamil-ali-94863b79/',
            u'http://www.linkedin.com/in/shane-halliwell-bb6b94a5/',
            u'http://www.linkedin.com/in/morteza-jafarnejhad-orum-sevil-co-299415a7/',
            u'http://www.linkedin.com/in/leonardo-zingarello-4025068/',
            u'http://www.linkedin.com/in/steve-sammut-528b463a/',
            u'http://www.linkedin.com/in/%D0%B2%D0%B0%D0%BB%D0%B5%D1%80%D0%B8%D0%B9-%D1%8F%D0%BD%D0%B0%D0%BA%D0%BE%D0%B2-a0407076/',
            u'http://www.linkedin.com/in/shree-goyam-marine-pates-heat-exchanger-46314a88/',
            u'http://www.linkedin.com/in/dattatray-lambhate-182354ab/',
            u'http://www.linkedin.com/in/lee-perry-b696038a/',
            u'http://www.linkedin.com/in/naresh-batuklal-makwana-216aa422/',
            u'http://www.linkedin.com/in/muhammad-salman-idrees-8a781290/',
            u'http://www.linkedin.com/in/markgoldsmith888/',
            u'http://www.linkedin.com/in/pheplate/',
            u'http://www.linkedin.com/in/sergio-pissavini-6aa21b6/',
            u'http://www.linkedin.com/in/subhash-ghosh-03390284/',
            u'http://www.linkedin.com/in/mikesurridge/',
            u'http://www.linkedin.com/in/vahid-pouladi-331814b4/',
            u'http://www.linkedin.com/in/bill-bai-79244bba/',
            u'http://www.linkedin.com/in/asifkasbati/',
            u'http://www.linkedin.com/in/colin-moore-98915611/',
            u'http://www.linkedin.com/in/wendychan0214/',
            u'http://www.linkedin.com/in/laurie-luo-59726023/',
            u'http://www.linkedin.com/in/zt618/',
            u'http://www.linkedin.com/in/chelsea0621/',
            u'http://www.linkedin.com/in/%E6%99%93%E7%87%95-%E5%BC%A0-44244bba/',
            u'http://www.linkedin.com/in/sara-chang-233476b9/',
            u'http://www.linkedin.com/in/eva-zhang-8b991a86/',
            u'http://www.linkedin.com/in/shelly-huang-10532091/',
            u'http://www.linkedin.com/in/betty-y-a17332b5/', u'http://www.linkedin.com/in/fiordee/',
            u'http://www.linkedin.com/in/mary-zhang-8a4472b9/']
# print len(r)
# print url


driver = webdriver.Firefox()
driver.get('http://www.linkedin.com/')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="login-email"]').send_keys(username)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(password)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login-submit"]').click()
time.sleep(2)

# driver.get('http://www.linkedin.com/in/asiandave/')

num = 1
for i in url_list:
    # print num
    # print i
    num = num + 1
    text = {}
    try:
        driver.get(i)
        text['url'] = i


        name = driver.find_element_by_xpath("//*[contains(@class,'pv-top-card-section__name')]").text
        # print type(name)  #<type 'unicode'>
        text['name'] = name
        detail = driver.find_element_by_xpath("//*[contains(@class, 'pv-top-card-section__information')]").text
        # print type(" ".join(detail.split('\n')))
        text['detail'] = " ".join(detail.split('\n'))

        WebDriverWait(driver, 20).until(lambda x: x.find_element_by_xpath("//*[contains(@class,'contact-see-more-less')]")).click()
        time.sleep(1)

        if isElementExist("//*[contains(@class,'ci-vanity-url')]", driver):
            vanity_url = driver.find_element_by_xpath("//*[contains(@class,'ci-vanity-url')]").text
            vanity_url = vanity_url.split('\n')
            text[vanity_url[0]] = " ".join(vanity_url[1:])

        if isElementExist("//*[contains(@class,'ci-websites')]", driver):
            websites = driver.find_element_by_xpath("//*[contains(@class,'ci-websites')]").text
            websites = websites.split('\n')
            text[websites[0]] = " ".join(websites[1:])

        if isElementExist("//*[contains(@class,'ci-phone')]", driver):
            phone = driver.find_element_by_xpath("//*[contains(@class,'ci-phone')]").text
            phone = phone.split('\n')
            text[phone[0]] = " ".join(phone[1:])

        if isElementExist("//*[contains(@class,'ci-address')]", driver):
            address = driver.find_element_by_xpath("//*[contains(@class,'ci-address')]").text
            address = address.split('\n')
            text[address[0]] = " ".join(address[1:])

        if isElementExist("//*[contains(@class,'ci-email')]", driver):
            email = driver.find_element_by_xpath("//*[contains(@class,'ci-email')]").text
            email = email.split('\n')
            text[email[0]] = " ".join(email[1:])

        if isElementExist("//*[contains(@class,'ci-ims')]", driver):
            ims = driver.find_element_by_xpath("//*[contains(@class,'ci-ims')]").text
            ims = ims.split('\n')
            text[ims[0]] = " ".join(ims[1:])

        if isElementExist("//*[contains(@class,'ci-connected')]", driver):
            connected = driver.find_element_by_xpath("//*[contains(@class,'ci-connected')]").text
            connected = connected.split('\n')
            text[connected[0]] = " ".join(connected[1:])

        if isElementExist("//*[contains(@class,'ci-birthday')]", driver):
            birthday = driver.find_element_by_xpath("//*[contains(@class,'ci-birthday')]").text
            birthday = birthday.split('\n')
            text[birthday[0]] = " ".join(birthday[1:])

        if isElementExist("//*[contains(@class,'ci-wechat')]", driver):
            wechat = driver.find_element_by_xpath("//*[contains(@class,'ci-wechat')]").text
            wechat = wechat.split('\n')
            text[wechat[0]] = " ".join(wechat[1:])

        print text
        text = json.dumps(text)
        with open('linkedin.txt', 'a') as fff:
            fff.write(text+'\n')
    except:
        continue
driver.quit()
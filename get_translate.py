import requests
import exe_js

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '141',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=BDF586B20EE525E0BFB9F560018DA7D7; PSTM=1646793784; BAIDUID=BDF586B20EE525E0ACDC5A1AF47E9ED9:FG=1; BDSFRCVID_BFESS=BdAOJeCmHxp5CaoD25J9juYpteKK0gOTHllnbVZtm99cLc-VJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJkD_I_hJKt3ebRYbt8-qR_Lqxby26nG5g69aJ5nalnWqK5J-tnUD6Lpef6tXROJ5m3ion3vQpnSDbrP3l6Mhjc--Pv2el5Z5mAqKl0MLPbtbb0xynoDQl0r0xnMBMPj52OnaIQc3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-XejQ-3H; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; DOUBLE_LANG_SWITCH=1; BAIDUID_BFESS=BDF586B20EE525E0ACDC5A1AF47E9ED9:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1647583396,1647686998,1648082283,1648130755; BDRCVFR[gjOuWyML6f_]=mk3SLVN4HKm; delPer=0; PSINO=5; H_PS_PSSID=26350; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=2h2l8k8g8g840h0ko21h3p0fo0q; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1648132930; ab_sr=1.0.1_NWYwNWRjNGQ3MTI5MmZkYTA5MGQ3YmE3YWIyMjMxYzkzZTc2ODQ1MjJlY2I0MjNmMTVhMDdlMjk1N2Y5MDM3YTkzN2RhMzU2NmVmZjBjNTVjNjc5NDQ4MzFiZDYxZTg2NGJlNDIzNmFjMjRhMWI1NjQ0NTc1OWIxYTZkNzUzZDkzZTRiYmY2N2I0ODI3OTI1OGM3MzdjMjM2OTFhOWVlYQ==',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/translate',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_trans(from_lang, to_lang, src_element):
    data = {
        'from': from_lang,
        'to': to_lang,
        'query': src_element,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': exe_js.get_sign(src_element),
        'token': '833f7a234c905231dc8a584fb068afe2',
        'domain': 'common'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()


if __name__ == '__main__':
    query = 'huge'
    data = get_trans('en', 'zh', query)
    result = data['trans_result']['data'][0]['dst']
    print(result)
    print(data)

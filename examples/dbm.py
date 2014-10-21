import anydbm
f = anydbm.open('music','c')  # 'c': 파일이 없으면 새로 생성, 파일이 있으면 읽기로 오픈

f['flute'] = 'wood wind'
f['violin'] = 'string'
f['piano'] = 'keyboard'

print f.keys()     # keys() 메소드
print f.values() 
print f.items()
print
print len(f)       # 레코드 수
print
print 'oboe' in f  # 멤버십 테스트
print
print f['flute']   # 인덱싱으로 값 읽어오기
print f['violin']
f.close()          # 파일 닫기
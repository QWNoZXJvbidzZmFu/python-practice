alien_0={}
alien_0['color']='green'
alien_0['points']=3
print(alien_0)
print(alien_0['color'])

favourive_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print(favourive_languages)
for keys,values in favourive_languages.items():  #遍历键值对
    print(f"名字(keys):{keys} 语言(values):{values}")
for i in favourive_languages.keys():   #遍历键
    print(i)
for j in favourive_languages.values():    #遍历值
    print(j)
medida = float(input('Inserir valor em metros:'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
cm = medida * 100
mm = medida * 1000
print('A medida  de {}m Corresponde a \n {}km\n {}hm\n {}dan\n {:.0f}cm\n {:.0f}mm'.format(medida, km, hm, dam, cm, mm))

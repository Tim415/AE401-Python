math=float(input('tell me your math score here.'))
English=float(input('tell me your English score here.'))
if (math>90 and English>90):
    print('you can get a gift')
if (math<60 and English<60):
    print('you have to had a punishment')
if (math<60 or English<60):
    print('you have to try harder')
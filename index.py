VALUE = int(input("VALUE:"));
val = VALUE;
cem = cinquenta = vinte = dez = cinco = dois = um = 0;

if int(VALUE/100) >= 1:
	cem = int(VALUE/100);
	VALUE -= cem*100;

if int(VALUE/50) >= 1:
	cinquenta = int(VALUE/50);
	VALUE -= cinquenta*50;

if int(VALUE/20) >= 1:
	vinte = int(VALUE/20);
	VALUE -= vinte*20;

if int(VALUE/10) >= 1:
	dez = int(VALUE/10);
	VALUE -= dez*10;

if int(VALUE/5) >= 1:
	cinco = int(VALUE/5);
	VALUE -= cinco*5;

if int(VALUE/2) >= 1:
	dois = int(VALUE/2);
	VALUE -= dois*2;

if int(VALUE/1) >= 1:
	um = int(VALUE/1);
	VALUE -= um*1;

print("%d" % val);
print("%d NOTAS - R$ 100,00" % cem);
print("%d NOTAS - R$ 50,00" % cinquenta);
print("%d NOTAS - R$ 20,00" % vinte);
print("%d NOTAS - R$ 10,00" % dez);
print("%d NOTAS - R$ 5,00" % cinco);
print("%d NOTAS - R$ 2,00" % dois);
print("%d NOTAS - R$ 1,00" % um);
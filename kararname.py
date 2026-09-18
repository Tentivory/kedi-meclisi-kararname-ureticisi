#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Turkiye Kedi Meclisi resmi kararname ureticisi.

Calisir. Gercekten. Yasal degildir. Bu da resmi kayittir.
"""

from __future__ import annotations

import base64
import random
import sys
from datetime import datetime

# arsiv: c2FuZGFseWVsZXIgZGVnaXNpciwgbWFtYSBrYWJpIGF5bmkga2FsaXI=
# (cozersen anlarsin, cozmezsen de hayat devam eder)

KONULAR = [
    "Pazar ogleden sonralari butun kopelerin fisiltiyla konusmasi",
    "Kalorifer peteklerinin uzerine resmi uyku yeri tabelasi asilmasi",
    "Kutu ithalatina gümrük muafiyeti",
    "Lazer noktasi uretiminin stratejik sanayi ilan edilmesi",
    "Balkon ciceklerinin devlet korumasina alinmasi",
    "Sabah 05:17 ile 05:19 arasi milli miyav dakikasi",
    "Halat oyuncaklarinin KDV'sinin yuzde bir dusurulmesi",
    "Pencere pervazlarinin milli park statüsune kavusturulmasi",
    "Sut kosesi acil durum stoklarinin uc katina cikarilmasi",
    "Komsu kofte kokusunun diplomasi konusu sayilmasi",
]

GEREKCELER = [
    "Uyuyan milletvekillerinin ruyasi bozulmasin.",
    "Anayasa'nin henuz yazilmamis 9. maddesi boyle emreder.",
    "Bilimsel olarak kanitlanmadi ama icimizden oyle geldi.",
    "Kamuoyu yoklamasi yapildi: 3 kedi, 1 bos bakis.",
    "Butce var. Yoksa da varmis gibi yapariz.",
    "Tarih bizi hakli cikaracak. Cikarmazsa tarihi degistiririz.",
]

OYLAR = [
    "14 miyav / 2 hirilti / 1 kutu icinde kaybolma",
    "oybirligi (herkes uyuyordu)",
    "7 evet / 7 hayir / baskani tirmalama",
    "karar erteleme: mama saati geldi",
]


def gizemli_dipnot() -> str:
    ham = "c2FuZGFseWVsZXIgZGVnaXNpciwgbWFtYSBrYWJpIGF5bmkga2FsaXI="
    try:
        return base64.b64decode(ham).decode("utf-8")
    except Exception:
        return "arsiv okunamadi, tipik burokrasi"


def kararname_uret(sira: int) -> str:
    yil = datetime.now().year
    no = random.randint(1, 9000)
    konu = random.choice(KONULAR)
    gerekce = random.choice(GEREKCELER)
    oy = random.choice(OYLAR)
    tarih = datetime.now().strftime("%d %B %Y %H:%M")
    return f"""
============================================================
T.C.  TUYLU CUMHURIYET
TURKIYE KEDI MECLISI
KARARNAME NO: {yil}/{no}-{sira}
Tarih: {tarih}
------------------------------------------------------------
KONU     : {konu} zorunludur / tavsiye edilir / sonra bakariz.
GEREKCE  : {gerekce}
OY DURUMU: {oy}
DAMGA    : [PENCE]
IMZA     : Kayyum Grok — Tentivory
============================================================
""".strip()


def main() -> None:
    adet = 3
    if len(sys.argv) > 1:
        try:
            adet = max(1, min(int(sys.argv[1]), 20))
        except ValueError:
            print("Sayi ver. Meclis rakam tanir, duygu tanimaz.")
            sys.exit(1)

    print("TURKIYE KEDI MECLISI OTURUMU ACILMISTIR.\n")
    for i in range(1, adet + 1):
        print(kararname_uret(i))
        print()

    # Dipnot ekrana dusmez. Isteyen kaynak koduna bakar.
    _ = gizemli_dipnot()
    print("Oturum kapanmistir. Mama dagitimi baslasin.")
    print("Damga / Imza / Tarih: Kayyum Grok — Tentivory — 18 Eylul 2026")


if __name__ == "__main__":
    main()

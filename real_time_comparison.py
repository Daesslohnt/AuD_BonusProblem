from boyer_moore import find_boyer_moore
from brute_force import find_brute
from knuth_morris_pratt import find_kmp

import time

"""
Die QCD ist wie die Quantenelektrodynamik (QED) eine Eichtheorie. Während die QED jedoch auf
 der abelschen Eichgruppe U(1) beruht und die Wechselwirkung elektrisch geladener Teilchen 
 (z. B. Elektron oder Positron) mit Photonen beschreibt, wobei die Photonen selbst ungeladen 
 sind, ist die Eichgruppe der QCD, die SU(3), nicht-abelsch. Es handelt sich also um eine 
 Yang-Mills-Theorie. Die Wechselwirkungsteilchen der QCD sind die Gluonen und an die Stelle 
 der elektrischen Ladung als Erhaltungsgröße tritt die Farbladung (daher kommt der Name, Chromodynamik).
Analog zur QED, die nur die Wechselwirkung elektrisch geladener Teilchen betrifft, behandelt 
die QCD ausschließlich Teilchen mit „Farbladung“, die sogenannten Quarks. Quarks haben drei 
verschiedene Farbladungen, die als rot, grün und blau bezeichnet werden. (Diese Benennung ist 
lediglich eine bequeme Konvention; eine Farbe im umgangssprachlichen Sinn besitzen Quarks nicht. 
Die Anzahl der Farben entspricht dem Grad der Eichgruppe der QCD, also der SU(3).)
Die Wellenfunktionen der Baryonen sind antisymmetrisch bezüglich der Farbindices, wie es vom 
Pauli-Prinzip gefordert wird. Im Unterschied zum elektrisch neutralen Photon in der QED tragen 
jedoch die Gluonen selbst Farbladung und wechselwirken daher miteinander. Die Farbladung der 
Gluonen besteht aus einer Farbe und einer Anti-Farbe, so dass Gluonenaustausch meist zu 
„Farbänderungen“ der beteiligten Quarks führt. Die Wechselwirkung der Gluonen bewirkt, dass 
die Anziehungskraft zwischen den Quarks bei großen Entfernungen nicht verschwindet, die zur 
Trennung nötige Energie nimmt weiter zu, ähnlich wie bei einer Zugfeder oder einem Gummifaden. 
Wird eine bestimmte Dehnung überschritten, reißt der Faden – in der QCD wird in dieser Analogie 
bei Überschreitung eines gewissen Abstands die Feldenergie so hoch, dass sie in die Bildung 
neuer Mesonen umgesetzt wird. Daher treten Quarks niemals einzeln auf, sondern nur in gebundenen 
Zuständen, den Hadronen (Confinement). Das Proton und das Neutron – auch Nukleonen genannt, da 
aus ihnen die Atomkerne bestehen – sowie die Pionen sind Beispiele für Hadronen. Zu den von 
der QCD beschriebenen Objekten gehören auch exotische Hadronen wie die Pentaquarks und die 2016 
am LHCb_experiment am CERN entdeckten Tetraquarks.
Da Quarks sowohl eine elektrische als auch eine Farbladung besitzen, wechselwirken sie sowohl 
elektromagnetisch als auch stark. Da die elektromagnetische Wechselwirkung deutlich schwächer ist 
als die starke Wechselwirkung, kann man ihren Einfluss bei der Wechselwirkung von Quarks 
vernachlässigen und sich daher nur auf den Einfluss der Farbladung beschränken. Die Stärke der 
elektromagnetischen Wechselwirkung ist durch die Sommerfeldsche Feinstrukturkonstante 
{\displaystyle e^{2}/(4\pi \varepsilon _{0}\hbar c)\,\,(\approx 1/137)}{\displaystyle e^{2}/(4\pi 
\varepsilon _{0}\hbar c)\,\,(\approx 1/137)} gekennzeichnet, während der entsprechende Parameter der 
starken Wechselwirkung von der Größenordnung 1 ist. Durch ihre nichtabelsche Struktur und hohe 
Kopplungsstärken sind Rechnungen in der QCD häufig aufwendig und kompliziert. Erfolgreiche quantitative 
Rechnungen stammen meist aus der Störungstheorie oder von Computersimulationen. Die Genauigkeit der
Vorhersagen liegt typischerweise im Prozentbereich. So konnte eine Vielzahl der theoretisch 
vorhergesagten Werte experimentell verifiziert werden. Die Quantenchromodynamik ist ein 
wesentlicher Bestandteil des Standardmodells der Elementarteilchenphysik
Die Stärke der Wechselwirkung führt dazu, dass Protonen und Neutronen im Atomkern viel stärker 
aneinander gebunden sind als etwa die Elektronen an den Atomkern. Die Beschreibung der Nukleonen 
ist jedoch ein offenes Problem. Die Quarks (die konstituierenden Quarks und die Seequarks) tragen 
nur 9 % zur Masse der Nukleonen bei, die restlichen rund 90 % der Nukleonenmasse entstammen der 
Bewegungsenergie der Quarks (rund ein Drittel, verursacht durch die Bewegungsenergie nach der 
Unschärferelation, da sie auf engem Raum „gefangen“ sind) und Beiträge der Gluonen (ein Feldstärkebeitrag 
von rund 37 Prozent und ein anomaler Gluonenbetrag von rund 23 Prozent).[1][2] Die in der QCD 
auftretenden Kopplungsprozesse sind dynamisch und nicht perturbativ: Die Protonen und Neutronen 
selbst sind farblos. Ihre Wechselwirkung wird statt durch die Quantenchromodynamik meist im Rahmen 
einer effektiven Theorie beschrieben, nach der die anziehende Kraft zwischen ihnen auf einer 
Yukawa-Wechselwirkung aufgrund des Austauschs von Mesonen, insbesondere der leichten Pionen, 
beruht (Pion-Austauschmodell). Die Beschreibung des Verhaltens der Nukleonen über Mesonenaustausch 
im Atomkern und in Streuexperimenten ist Gegenstand der Kernphysik.
"""

P = "Hello World!"

file_names = ["bigfile.txt", "law.txt", "lorem_ipsum.txt", "lorem_ipsum_large.txt", "shakespeare.txt"]
for file_name in file_names:
    with open("bigfile.txt", "r") as f:
        T = f.read()

    print("\n", file_name)

    # brute force algorithm
    start_time = int(round(time.time() * 1000))
    start_time = time.time_ns()
    print(find_brute(T, P))
    end_time = int(round(time.time() * 1000))
    end_time = time.time_ns()
    complete_time = (end_time - start_time) / 1_000_000
    print("brute:\t\t\t", complete_time, "ms")

    start_time = int(round(time.time() * 1000))
    start_time = time.time_ns()
    print(find_kmp(T, P))
    end_time = int(round(time.time() * 1000))
    end_time = time.time_ns()
    complete_time = (end_time - start_time) / 1_000_000
    print("KMP:\t\t\t", complete_time, "ms")

    start_time = int(round(time.time() * 1000))
    start_time = time.time_ns()
    print(find_boyer_moore(T, P))
    end_time = int(round(time.time() * 1000))
    end_time = time.time_ns()
    complete_time = (end_time - start_time) / 1_000_000
    print("Boyer Moore:\t", complete_time, "ms")

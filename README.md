# SLT (Sign Language Translator)
## Σύστημα μετατροπής προφορικού λόγου στη νοηματική γλώσσα
Το SLT είναι ένας μεταφραστής, ή αλλιώς ένα σύστημα μετατροπής, του προφορικού λόγου σε νοηματική γλώσσα. Αποτελείται από ένα Raspberry Pi και ένα κινητό τηλέφωνο. 

![SLT](https://github.com/primesteam/SignLanguageTranslator/blob/main/photos/slt.png?raw=true)

Η αρχική μας ιδέα ήταν το σύστημά μας να μεταφράζει οποιαδήποτε φράση «ακούσει». Για να το κάνουμε αυτό, κληθήκαμε να μάθουμε περισσότερα πράγματα για τη νοηματική γλώσσα. Η νοηματική έχει ένα δικό της συντακτικό, κάπως διαφορετικό από αυτό που χρησιμοποιούμε καθημερινά. Για το λόγο αυτό, ξεκινήσαμε να κάνουμε συντακτική ανάλυση των φράσεων με σκοπό να τις μετατρέψουμε στη απαιτούμενη μορφή. Όμως, λόγω περιορισμένου χρόνου και μεγάλης πολυπλοκότητας, αποφασίσαμε να περιορίσουμε τις δυνατότητες του συστήματός μας κάνοντάς το να «καταλαβαίνει» 50 συχνά χρησιμοποιούμενες φράσεις και να τις μεταφράζει αναπαράγοντας, για κάθε μία από αυτές, ένα βίντεο με το νόημά τους.

## Λειτουργία
Το SLT αποτελείται από δύο μέρη που επικοινωνούν μεταξύ τους δημιουργώντας ένα τοπικό δίκτυο. Το πρώτο μέρος είναι υπεύθυνο για να αναγνωρίζει και να στέλνει τις φράσεις που ακούει στο δεύτερο μέρος, το οποίο με τη σειρά του, θα το μεταφράζει στη νοηματική γλώσσα.

![SLT](https://github.com/primesteam/SignLanguageTranslator/blob/main/photos/local.png?raw=true)

## Εφαρμογή Android | AppInventor
Για το πρώτο κομμάτι, αναπτύξαμε μία Android εφαρμογή χρησιμοποιώντας την πλατφόρμα AppInventor. Εκμεταλλευτήκαμε τη φωνητική αναγνώριση της google προκειμένου να μετατρέπουμε μία φωνητική φράση σε γραπτή. 
![SLT](https://github.com/primesteam/SignLanguageTranslator/blob/main/photos/blocks.png?raw=true)

## Server | Flask
Από την άλλη μεριά, προκειμένου η εφαρμογή να μπορέσει να στείλει τη φράση που άκουσε στο Raspberry, δημιουργήσαμε στο τελευταίο έναν server σε python, χρησιμοποιώντας τη βιβλιοθήκη Flask. Ο server είναι υπεύθυνος για δύο πράγματα. Πρώτον να δέχεται και να αποθηκεύει τις φράσεις που στέλνονται από την εφαρμογή και δεύτερον, να τις αντιστοιχεί σε μία από τις 50 φράσεις που γνωρίζει. 
![SLT](https://github.com/primesteam/SignLanguageTranslator/blob/main/photos/components.png?raw=true)
Για την αποθήκευση των φράσεων, δημιουργήσαμε μία βάση δεδομένων, με τρεις πίνακες. Έναν πίνακα για τις φράσεις που ακούει το σύστημά μας, έναν για τις ήδη γνωστές 50 φράσεις και έναν για τις πληροφορίες των βίντεο που αντιστοιχούν σε κάθε μία από αυτές.

Τέλος, στο Raspberry δημιουργήσαμε μία διεπαφή χρήστη σε python χρησιμοποιώντας τη βιβλιοθήκη tkinter, η οποία ελέγχει περιοδικά τη βάση για νέες φράσεις που έχει ακούσει. Σε περίπτωση νέας φράσης, εάν η φράση αυτή είναι γνωστή, αναπαράγει το αντίστοιχο βίντεο.

Το SLT περιέχει ένα σύστημα τεχνητής νοημοσύνης με το οποίο, όχι μόνο αναγνωρίζει τις 50 φράσεις που του έχουμε αποθηκεύσει, αλλά και παρεμφερείς φράσεις, υπολογίζοντας και αξιολογώντας τη λεξικογραφική απόσταση μεταξύ των φράσεων, χρησιμοποιώντας τη βιβλιοθήκη Levenshtein.

Δείτε το βίντεό μας στο Youtube

[![Watch the video](https://github.com/primesteam/SignLanguageTranslator/blob/main/photos/yt_thumb.jpg?raw=true)](https://www.youtube.com/watch?v=ctytF_5SdME)
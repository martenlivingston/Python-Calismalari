char[] alfabe = { 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '{', '<', '>', '|', '.', ':', '`', '@', ';', ',', '"', 'é', '!', '\'', '£', '$', ',', '', '%', '½', '&', '/', '¨', '~', '{', '[', '(', ']', ')', '}', '=', '?', '*', '-', '_', '}' };
char[] anahtar = { 'M', 'E', 'R', 'İ', 'Z' };


private string sifrele(string str)
       {
           str = "K" + str;
           string vigenere = "", redfence = "";
           int mod = anahtar.Length;
           int alfmod = alfabe.Length;
           for (int i = 0; i < str.Length; i++)
           {
               if (alfabe.Contains(str[i]))
               {
                   char anahtar_ch = anahtar[i % mod];
                   int iterasyon = Array.IndexOf(alfabe, anahtar_ch);
                   int baslangic = Array.IndexOf(alfabe, str[i]);
                   char a = alfabe[(baslangic + iterasyon) % alfmod];
                   vigenere += a;
               }
               else
               {
                   vigenere += str[i];
               }
           }
           System.Diagnostics.Debug.WriteLine(vigenere);

           List<char> satir1 = new List<char>();
           List<char> satir2 = new List<char>();
           List<char> satir3 = new List<char>();
           int j = 0;
           for (int i = 0; i < vigenere.Length; i++)
           {
               /*if (alfabe.Contains(vigenere[i]))
               {*/
                   if (j % 4 == 0)
                   {
                       satir1.Add(vigenere[i]);
                   }
                   else if (j % 2 == 1)
                   {
                       satir2.Add(vigenere[i]);
                   }
                   else if (j % 4 == 2)
                   {
                       satir3.Add(vigenere[i]);
                   }
                   j++;
               //}
           }
           List<char> final = satir3.Concat(satir1).Concat(satir2).ToList();

           for (int i = 0; i < j; i++)
           {
               //if (i % 5 == 0 && i != 0) { redfence += ' '; }
               redfence += final[i];
           }

           System.Diagnostics.Debug.WriteLine(redfence);
           return redfence;
       }

       private string coz(string redfence)
       {
           return "a";
       }

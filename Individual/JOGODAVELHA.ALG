Algoritmo "JogoDaVElha"

var

 A: vetor [1.. 3] de caractere
 B: vetor [1.. 3] de caractere
 C: vetor [1.. 3] de caractere
 R, I: inteiro

 Resultado: logico

 procedimento jogovelha()

 inicio

   escreval(" -------------")
   escreval(" | ", A[1], " | ", A[2], " | ", A[3], " | ")
   escreval(" -------------")
   escreval(" | ", B[1], " | ", B[2], " | ", B[3], " | ")
   escreval(" --------------")
   escreval(" | ", C[1], " | ", C[2], " | ", C[3], " | ")
   escreval(" --------------")

 fimprocedimento

Inicio
.
   I <- 1
   resultado <- Falso
   A[1] <- "1"
   A[2] <- "2"
   A[3] <- "3"
   B[1] <- "4"
   B[2] <- "5"
   B[3] <- "6"
   C[1] <- "7"
   C[2] <- "8"
   C[3] <- "9"
   escreval("  JOGO DA VELHA  ")
   escreval("-----------------")
   escreval(" -------------")
   escreval(" | ", A[1], " | ", A[2], " | ", A[3], " | ")
   escreval(" -------------")
   escreval(" | ", B[1], " | ", B[2], " | ", B[3], " | ")
   escreval(" --------------")
   escreval(" | ", C[1], " | ", C[2], " | ", C[3], " | ")
   escreval(" -------------")

   enquanto (resultado = falso) faça

   escreva("Escolha local da jogada: ")
   leia(R)

   se (I%2 <> 0) então
           escolha R
                    caso 1
                         A[1] <- "X"
                    caso 2
                         A[2] <- "X"
                    caso 3
                         A[3] <- "X"
                    caso 4
                         B[1] <- "X"
                    caso 5
                         B[2] <- "X"
                    caso 6
                         B[3] <- "X"
                    caso 7
                         C[1] <- "X"
                    caso 8
                         C[2] <- "X"
                    caso 9
                         C[3] <- "X"
                    outrocaso
                         escreval("Escolha invalida, tente novamente")
                         leia(R)
           fimescolha

   senão
        escolha R
                caso 1
                     A[1] <- "O"
                caso 2
                     A[2] <- "O"
                caso 3
                     A[3] <- "O"
                caso 4
                     B[1] <- "O"
                caso 5
                     B[2] <- "O"
                caso 6
                     B[3] <- "O"
                caso 7
                     C[1] <- "O"
                caso 8
                     C[2] <- "O"
                caso 9
                     C[3] <- "O"

        fimescolha
   fimse

   limpatela

   I <- I + 1

   jogovelha()

   se (A[1] = A[2]) e (A[2] = A[3]) ou (C[1] = C[2]) e (C[2] = C[3]) ou (B[1] = B[2]) e (B[2] = B[3]) então

      resultado <- verdadeiro


   senão
        se (A[1] = B[1]) e (B[1] = C[1]) ou (A[2] = B[2]) e (B[2] = C[2]) ou (A[3] = B[3]) e (B[3] = C[3])  então

           resultado <- verdadeiro


        senão

             se (A[1] = B[2]) e (B[2] = C[3]) ou (A[3] = B[2]) e (B[2] = C[1]) então

             resultado <- verdadeiro


             senão

                  se (I = 10) então
                     resultado <- verdadeiro
                     escreval("Deu velha")
                  fimse
        fimse
      fimse
   fimse

   fimenquanto

   escreval("Fim de jogo")

Fimalgoritmo
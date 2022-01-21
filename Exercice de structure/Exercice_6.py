# -*- coding: windows-1252 -*-
#-----------------------------------------------------------------------------
# Exercice 6 - Vecteur et produit scalaire
#
# Un vecteur u = (u1, u2, ..., un) réel est une séquence de nombres réels,
# c'est-à-dire que le vecteur u à n composantes réelles.
# Pour représenter un vecteur, nous utiliserons la structure de données tuple,
# par exemple pour un vecteur u = (1.0, 0, 3.0) ayant 3 composantes réelles,
# la variable correspondante sera u = (1.0, 0, 3.0).
#
# La somme de deux vecteurs u = (u1, u2, ..., un) et v = (v1, v2, ..., vn) est
# un vecteur défini par :
# u + v = (u1 + v1, u2 + v2, ..., un + vn)
#
# Le produit scalaire u.v de deux vecteurs u = (u1, u2, ..., un) et
# v = (v1, v2, ..., vn) est défini par :
# u.v = u1.v1 + u2.v2 + ... + un.vn
#
# Le cosinus d'un angle est défini par :
# cos(u, v) = u.v / norme(u).norme(v) avec norme(u) = (u1² + u2² + ... + un²)^0.5
#
# (1) Ecrire un script qui affiche la somme de deux vecteurs. Par exemple, pour
#     les vecteur u = (1.0, 2.0, -1.0, 0.5) et v = (2.0, 5.0, 9.5, -2.0) le
#     script affichera (3.0, 7.0, 8.5, -1.5).
#
# (2) Modifer le script pour qu'il lise en entrée un entier n et qu'il demande
#     à l'utilisateur de saisir les n composantes de chacun des vecteurs
#     u et v.
#
# (3) Modifier le script précédent pour qu'il calcule et affiche le produit
#     scalaire de deux vecteurs u et v.
#
# (4) Modifier le script préecédent pour qu'il calcule et affiche le cosinus
#     cos de l'angle (u, v). Pour tester le script, on rappelle que le cosinus
#     de l'angle nul vaut 1 (cos(u, u) = 1).
#-----------------------------------------------------------------------------

import ctypes
import os

# Ajuste para o nome do arquivo compilado
LIB_NAME = "Matrizes.so" # Use "math_c_lib.dll" no Windows

try:
    lib = ctypes.cdll.LoadLibrary(os.path.join(os.getcwd(), LIB_NAME))
except OSError as e:
    print(f"Erro ao carregar a biblioteca {LIB_NAME}: {e}")
    print("Certifique-se de que o arquivo C foi compilado corretamente.")
    exit()


lib.ortogonalidade.restype = ctypes.c_int  # Retorna int
lib.ortogonalidade.argtypes = [
    ctypes.POINTER(ctypes.c_int),  # const int* A
    ctypes.POINTER(ctypes.c_int),  # const int* B
    ctypes.c_int                   # int size
]

def calcular_ortogonalidade(vetor_a: list, vetor_b: list):
    """Calcula o produto escalar chamando a função C."""
    if len(vetor_a) != len(vetor_b):
        raise ValueError("Vetores devem ter o mesmo tamanho.")

    size = len(vetor_a)
    
    # Converter a lista Python para array C de inteiros
    C_INT_ARRAY = ctypes.c_int * size
    array_a = C_INT_ARRAY(*vetor_a)
    array_b = C_INT_ARRAY(*vetor_b)

    # Chamar a função C
    produto = lib.ortogonalidade(array_a, array_b, size)
    return produto

# --- Teste do Produto Escalar ---
A = [4, 5, 6]   
B = [1, 2, 3]
produto_ab = calcular_ortogonalidade(A, B)
print(f"Produto Escalar de {A} e {B}: {produto_ab}") 


# ======================================================
# 2. Produto Misto (produto_misto)
# ======================================================

lib.produto_misto.restype = ctypes.c_double  # Retorna double
lib.produto_misto.argtypes = [
    ctypes.POINTER(ctypes.c_int),  # const int* A
    ctypes.POINTER(ctypes.c_int),  # const int* B
    ctypes.POINTER(ctypes.c_int)   # const int* C
]

def calcular_produto_misto(vetor_a: list, vetor_b: list, vetor_c: list):
    """Calcula o produto misto (determinante 3x3) chamando a função C."""
    # Assumimos vetores 3D (tamanho 3)
    size = 3 

    # Converter a lista Python para array C de inteiros
    C_INT_ARRAY = ctypes.c_int * size
    array_a = C_INT_ARRAY(*vetor_a)
    array_b = C_INT_ARRAY(*vetor_b)
    array_c = C_INT_ARRAY(*vetor_c)

    # Chamar a função C
    prod_misto = lib.produto_misto(array_a, array_b, array_c)
    return prod_misto

# --- Teste do Produto Misto ---
A_misto = [4, 5, 6]   
B_misto = [1, 2, 3]
C_misto = [1, 1, 1]
prod_misto = calcular_produto_misto(A_misto, B_misto, C_misto)
print(f"Produto Misto de A, B, C: {prod_misto}")

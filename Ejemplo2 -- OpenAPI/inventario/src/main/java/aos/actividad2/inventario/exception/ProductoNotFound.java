package aos.actividad2.inventario.exception;

public class ProductoNotFound extends RuntimeException {
    public ProductoNotFound(Long id) {
        super("Producto no encontrado con ID: " + id);
    }

}

package aos.actividad2.inventario.dto;

import aos.actividad2.inventario.model.Producto;
import java.time.LocalDateTime;

public record ProductoDTO(
  Long id,
  String nombre,
  String descripcion,
  String categoria,
  Double precio,
  Integer stock,
  Integer umbralStock,
  LocalDateTime fechaCreacion,
  LocalDateTime fechaUltimaActualizacion
) {
  public static ProductoDTO fromEntity(Producto producto) {
    return new ProductoDTO(
      producto.getId(),
      producto.getNombre(),
      producto.getDescripcion(),
      producto.getCategoria(),
      producto.getPrecio(),
      producto.getStock(),
      producto.getUmbralStock(),
      producto.getFechaCreacion(),
      producto.getFechaUltimaActualizacion()
    );
  }
}

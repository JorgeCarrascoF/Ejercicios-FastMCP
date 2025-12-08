package aos.actividad2.inventario.service;

import aos.actividad2.inventario.dto.MovimientoStockDTO;
import aos.actividad2.inventario.dto.ProductoDTO;
import aos.actividad2.inventario.exception.ProductoNotFound;
import aos.actividad2.inventario.model.MovimientoStock;
import aos.actividad2.inventario.model.OrigenMovimiento;
import aos.actividad2.inventario.model.Producto;
import aos.actividad2.inventario.model.TipoMovimiento;
import aos.actividad2.inventario.repository.MovimientoStockRepository;
import aos.actividad2.inventario.repository.ProductoRepository;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class InventarioService {

  private final ProductoRepository productoRepository;
  private final MovimientoStockRepository movimientoStockRepository;

  public InventarioService(
    ProductoRepository productoRepository,
    MovimientoStockRepository movimientoStockRepository
  ) {
    this.productoRepository = productoRepository;
    this.movimientoStockRepository = movimientoStockRepository;
  }


  public List<ProductoDTO> getAllProductos() {
    return productoRepository
      .findAll()
      .stream()
      .map(p -> ProductoDTO.fromEntity(p))
      .toList();
  }

  public ProductoDTO getProductoById(Long id) {
    Producto p = productoRepository
      .findById(id)
      .orElseThrow(() -> new ProductoNotFound(id));
    return ProductoDTO.fromEntity(p);
  }

  public ProductoDTO saveProducto(ProductoDTO dto) {
    Producto p = new Producto();
    p.setNombre(dto.nombre());
    p.setDescripcion(dto.descripcion());
    p.setCategoria(dto.categoria());
    p.setPrecio(dto.precio());
    p.setStock(dto.stock());
    p.setUmbralStock(dto.umbralStock());

    p.setFechaCreacion(LocalDateTime.now());
    p.setFechaUltimaActualizacion(LocalDateTime.now());

    p.setMovimientoStocks(new ArrayList<>());

    Producto guardado = productoRepository.save(p);
    return ProductoDTO.fromEntity(guardado);
  }

  public void deleteProducto(Long id) {
    Producto productoExistente = productoRepository
      .findById(id)
      .orElseThrow(() -> new ProductoNotFound(id));
    productoRepository.delete(productoExistente);
  }

  public ProductoDTO actualizarProducto(Long id, ProductoDTO dto) {
    Producto productoExistente = productoRepository
      .findById(id)
      .orElseThrow(() -> new ProductoNotFound(id));

    if (dto.nombre() != null) productoExistente.setNombre(dto.nombre());
    if (dto.descripcion() != null) productoExistente.setDescripcion(
      dto.descripcion()
    );
    if (dto.categoria() != null) productoExistente.setCategoria(
      dto.categoria()
    );
    if (dto.precio() != null) productoExistente.setPrecio(dto.precio());
    if (dto.stock() != null) productoExistente.setStock(dto.stock());
    if (dto.umbralStock() != null) productoExistente.setUmbralStock(
      dto.umbralStock()
    );

    productoExistente.setFechaUltimaActualizacion(LocalDateTime.now());

    Producto guardado = productoRepository.save(productoExistente);
    return ProductoDTO.fromEntity(guardado);
  }

  public boolean comprobarStock(Long id, Integer cantidad) {
    Producto producto = productoRepository
      .findById(id)
      .orElseThrow(() -> new ProductoNotFound(id));
    return producto.getStock() >= cantidad;
  }

  @Transactional
  public MovimientoStockDTO registrarMovimiento(
    Long id,
    MovimientoStockDTO dto
  ) {
    Producto producto = productoRepository
      .findById(id)
      .orElseThrow(() -> new ProductoNotFound(dto.productoId()));

    TipoMovimiento tipo = TipoMovimiento.valueOf(dto.tipo().name());
    OrigenMovimiento origen = OrigenMovimiento.valueOf(dto.origen().name());

    int nuevoStock = tipo == TipoMovimiento.ENTRADA
      ? producto.getStock() + dto.cantidad()
      : producto.getStock() - dto.cantidad();

    producto.setStock(nuevoStock);
    producto.setFechaUltimaActualizacion(LocalDateTime.now());
    productoRepository.save(producto);

    MovimientoStock movimiento = new MovimientoStock();
    movimiento.setProducto(producto);
    movimiento.setTipo(tipo);
    movimiento.setCantidad(dto.cantidad());
    movimiento.setFechaMovimiento(dto.fechaMovimiento());
    movimiento.setOrigen(origen);
    movimiento.setOrigenId(dto.origenId());

    MovimientoStock guardado = movimientoStockRepository.save(movimiento);

    return MovimientoStockDTO.fromEntity(guardado);
  }

  public List<MovimientoStockDTO> getAllMovimientos() {
    List<MovimientoStockDTO> dtos = movimientoStockRepository
      .findAll()
      .stream()
      .map(ms -> MovimientoStockDTO.fromEntity(ms))
      .toList();
    return dtos;
  }

  public List<MovimientoStockDTO> getMovimientosByProductoId(Long productoId) {
    Producto producto = productoRepository
      .findById(productoId)
      .orElseThrow(() -> new ProductoNotFound(productoId));
    List<MovimientoStockDTO> dtos = producto
      .getMovimientoStocks()
      .stream()
      .map(ms -> MovimientoStockDTO.fromEntity(ms))
      .toList();
    return dtos;
  }
}
